
# pull official base image
FROM python:3.9.15-slim-buster

# set work directory
WORKDIR /home

# copy all the files to the container
COPY . .

# install dependencies
RUN \
pip install -r requierments.txt

EXPOSE 8000

# run the command
CMD ["python", "con_str-api-staging.py"]

