## Run

```
docker build -t gcp-serverless-python -f Dockerfile .

docker run -it -p 80:5000 gcp-serverless-python

docker run --env PORT=5000 -it -p 80:5000 gcp-serverless-python

```


## Push
### via Docker

```
docker build -t gcp-serverless-python -f Dockerfile .

docker tag gcp-serverless-python gcr.io/cfe-project-357217/gcp-serverless-python

docker push gcr.io/cfe-project-357217/gcp-serverless-python

```

### GCP IAM

Roles required by the service:
Cloud Build Service Agent
Container REgistry Service Agent
Storage Object Creator

### via GCloud Build

```
gcloud builds submit --tag gcr.io/cfe-project-357217/gcp-serverless-python:scrapper

```