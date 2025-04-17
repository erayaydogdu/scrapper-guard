
## Example Request

```code
curl -X POST -H "Content-Type: application/json" -d '{"content": "Global wine consumption decreased by over 3% last year to 214.2 million hectoliters, the lowest level since 1961", "field": "excerptAi", "collection-name": "singleNews", "date": "2025-04-17"}' http://localhost:5060/is-exist-in-db
```

docker build -t <your_dockerhub_username>/<image_name> 