
## Example Request

```code
curl -X POST -H "Content-Type: application/json" -d '{"content": "Global wine consumption decreased by over 3% last year to 214.2 million hectoliters, the lowest level since 1961", "field": "excerptAi", "collection-name": "singleNews", "date": "2025-04-17"}' -u sita:mypassword123 http://localhost:5060/is-exist-in-db
```

## Authentication

To use the `/is-exist-in-db` endpoint, you need to provide basic authentication credentials.

You can do this using the `-u` flag in curl, followed by the username and password separated by a colon:

```code
curl -X POST -H "Content-Type: application/json" -u <username>:<password> -d '{"content": "Global wine consumption decreased by over 3% last year to 214.2 million hectoliters, the lowest level since 1961", "field": "excerptAi", "collection-name": "singleNews", "date": "2025-04-17"}' http://localhost:5060/is-exist-in-db
```

Replace `<username>` and `<password>` with the actual username and password you have set in the `.env` file.

docker build -t <your_dockerhub_username>/<image_name>