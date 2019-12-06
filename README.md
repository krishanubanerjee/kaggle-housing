# kaggle-housing 
<br> Initial data exploration and model building is in jupyter notebook kaggle_housing_EDA_model_building.ipynb.<br>
 File train.py will build the model for docker using train.csv file . 
 File requirements.txt is used in docker for installing all required module.
Dockerfile is used creating docker container and image.
api.py  will create Rest api and using trained model and responsible for predicting online requests.
docker can be tested using posman where input is ten features (overall rating, floor area etc.) and output salesp price.
kaggle_docker_steps is showing the steps executed for docker and testing in postman.
