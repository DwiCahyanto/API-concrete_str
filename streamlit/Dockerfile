
# pull official base image
FROM python:3.10-slim

# set work directory
WORKDIR /home

# copy all the files to the container
COPY . .

# install dependencies
RUN \
pip install -r requierments.txt

EXPOSE 8501

# run the command
CMD ["streamlit", "run", "conc-streamlit.py"]

