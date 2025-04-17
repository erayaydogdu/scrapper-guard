import logging
from datetime import datetime
from sentence_transformers import SentenceTransformer
from db import get_all_data
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_posts(dateStr, collection_name):
    if not dateStr:
        today = datetime.now()
        dateStr = today.strftime("%Y-%m-%d")
    data = get_all_data(dateStr, collection_name)
    if data is None:
        logging.debug("Error: Could not load existing posts.")
        return []
    if not data:
        return [ {"externalId" : "1", "excerptAi" : "NewPost"} ]
    return data



def find_near_duplicates(new_text, existing_embeddings, threshold=0.70):
    new_post_embedding = model.encode([new_text])[0]
    similarities = model.similarity(existing_embeddings, new_post_embedding)
    return similarities

def print_similarity_result(similaritiesResult, existing_posts_texts, new_post):
    if any(s > 0.7 for s in similaritiesResult):
        logging.debug(f"\n'{new_post}' is a near-duplicate of:")
        for i, similarity in enumerate(similaritiesResult):
            if similarity > 0.7:
                logging.debug(f"- '{existing_posts_texts[i]['externalId']}' (Similarity: {similarity.item():.4f})")
    else:
        logging.debug(f"\n'{new_post}' is a new post.")

@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/is-exist-in-db', methods=['POST'])
def is_exist_in_db():
    try:
        data = request.get_json()
        content = data.get('content')
        field = data.get('field')
        date = data.get('date')
        collection_name = data.get('collection-name')

        if not all([content, field, collection_name, date]):
            return jsonify({"error": "Missing parameters"}), 400

        
        posts = load_posts(date,collection_name)
        posts_embeddings = model.encode([post[field] for post in posts])
        similaritiesResult = find_near_duplicates(content, posts_embeddings)

        if similaritiesResult is None:
            return jsonify({"error": "Could not calculate similarities."}), 500
        
        print_similarity_result(similaritiesResult, posts, content)

        duplicate_post_ids = []
        isNew = False
        if any(s > 0.7 for s in similaritiesResult):
            duplicate_post_ids = [posts[i]['externalId'] for i, similarity in enumerate(similaritiesResult) if similarity > 0.7]
        else:
            isNew = True

        result = {"duplicate_post_ids": duplicate_post_ids, "isNew": isNew}
        return jsonify(result), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500
        
        

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5060)
