FROM jupyter/scipy-notebook

RUN pip install joblib

RUN mkdir kaggle
ENV MODEL_DIR=/Users/krishanubanerjee/Documents/kaggle
ENV MODEL_FILE=rf.joblib
ENV METADATA_FILE=metadata.json

COPY train.csv ./train.csv
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY train.py ./train.py
COPY api.py ./api.py

RUN python3 train.py
