##!/bin/bash

# Variables
PROJECT_ID=sander-van-donkelaar-sndbx-v
IMAGE_NAME=maximai           
REGION=europe-west4            
SERVICE_NAME=maximai           
CONTAINER_PORT=8080                       

gcloud config set project $PROJECT_ID

# Deploy the container image to Cloud Run
gcloud run deploy $SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --port $CONTAINER_PORT \
  --allow-unauthenticated \
  --source .

