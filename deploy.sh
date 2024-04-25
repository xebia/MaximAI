##!/bin/bash

# Variables
PROJECT_ID=qwiklabs-gcp-02-c86bd22dbd03
IMAGE_NAME=maximai           
REGION=europe-west4            
SERVICE_NAME=maximai           
CONTAINER_PORT=8080                       

gcloud config set project $PROJECT_ID

# Deploy the container image to Cloud Run. Will create a new artifact registry. 
gcloud run deploy $SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --port $CONTAINER_PORT \
  --allow-unauthenticated \
  --min-instances=1 \
  --max-instances=1 \
  --source .

