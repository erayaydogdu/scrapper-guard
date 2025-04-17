import pymongo
import logging
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

logging.basicConfig(level=logging.DEBUG)

try:
    pass
except ImportError as e:
    pass

connection_string = os.getenv("MONGODB_URI")
database_name = os.getenv("MONGODB_DATABASE")


def get_all_data(date, collection_name):
    logging.debug(f"Connection:  {connection_string} - Database: {database_name} - Collection {collection_name}")
    try:
        client = pymongo.MongoClient(connection_string)
        db = client[database_name]
        collection = db[collection_name]
        stpdate = datetime.strptime(date, "%Y-%m-%d")
        filter = {
            "date": {
                "$gte": datetime(stpdate.year, stpdate.month, stpdate.day, 0, 0, 0, 0),
                "$lt": datetime(stpdate.year, stpdate.month, stpdate.day, 23, 59, 59, 999),
            }
        }
        logging.debug(f"Filter: {filter}")
        documents = list(collection.find(filter))
        if not documents:
            logging.debug("[ERAYNOTE] No documents found.")
            return []
        logging.debug(f"[ERAYNOTE] Found {len(documents)} documents.")
        return documents
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
    finally:
        client.close()