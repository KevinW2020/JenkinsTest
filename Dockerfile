# set base image (host OS)
FROM public.ecr.aws/lambda/python:3.7

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/WellsSearch.py .

# command to run on container start
CMD [ "WellsSearch.lambda_handler" ]
