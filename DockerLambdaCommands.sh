#!/bin/bash

# Builds the image
docker build -t lambda-container-3.7 .

# Tags the image
docker tag lambda-container-3.7 494942955538.dkr.ecr.us-east-1.amazonaws.com/lambda-container-demo

# Push to ECR as latest
docker push 494942955538.dkr.ecr.us-east-1.amazonaws.com/lambda-container-demo

# Delete an existing function if there is one
#aws lambda delete-function --function-name test

# Create the new test function
# aws lambda create-function --function-name LambdaContainer-WellLocation --package-type Image --code ImageUri=494942955538.dkr.ecr.us-east-1.amazonaws.com/lambda-container-demo:latest --role arn:aws:iam::494942955538:role/LambdaExecution-Containers --timeout 30

# #aws lambda update-function-code --function-name test --image-uri 494942955538.dkr.ecr.us east-1.amazonaws.com/lambda-container-demo:latest

# # Wait for 5 seconds
# sleep 5

# # Test function
# aws lambda invoke --function-name LambdaContainer-WellLocation --payload '{"City":"London"}' testResponse.json



