# kaggle-housing 
<br> Initial data exploration and model building is in jupyter notebook kaggle_housing_EDA_model_building.ipynb.<br>
 <br> File train.py will build the model for docker using train.csv file . <br>
 <br> File requirements.txt is used in docker for installing all required module.<br>
<br> Dockerfile is used creating docker container and image.<br>
<br> api.py  will create Rest api and using trained model and responsible for predicting online requests.<br>
<br> docker can be tested using posman where input is ten features (overall rating, floor area etc.) and output salesp price.<br>
<br> kaggle_docker_steps is showing the steps executed for docker and testing in postman.<br>

## How to run in remote machine 
<br> Install docker from https://hub.docker.com/ <br>
<br> Pull docker container to local machine -    Run from the command prompt -  docker pull bkrishanu/docker-api  <br>
<br> Run from command prompt -  docker run -it -p 5000:5000 docker-api python3 api.py  <br>
<br> It will show - <br>
<br> Loading model from: rf.joblib <br>
 <br> * Serving Flask app "api" (lazy loading) <br>
 <br> * Environment: production <br>
 <br> WARNING: This is a development server. Do not use it in a production deployment.<br>
 <br> Use a production WSGI server instead.<br>
 <br> * Debug mode: on <br>
 <br> * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) <br>
 <br> * Restarting with stat <br>
<br> Loading model from: rf.joblib <br>
 <br> * Debugger is active!<br>
 <br> * Debugger PIN: 620-881-786<br>
 ### Docker is running now
 <br> Download postman - https://www.getpostman.com/downloads/ <br>
 <br> In Postman, click - Create a Request <br>
 <br> Select POST , Enter url - {ip of the machine where you are running the docker image,use localhost if you run postman in same machine}:5000/predict <br>
 <br> Select body --> raw --> JSON <br>
 <br> Paste example like -
 { 
   "OverallQual":8,
   "GrLivArea":1068,
   "TotalBsmtSF":1059,
   "1stFlrSF":1068,
   "BsmtFinSF1":663,
   "GarageArea":264,
   "2ndFlrSF":0,
   "TotRmsAbvGrd":6,
   "LotArea":8414,
   "YearBuilt":1963
} <br>
<br> Enter SEND , you will get online prediction for new Salesv value . Change any parameters and/or send multiple requests 
to get different prediction.Please note, if json file is corrupted then need to correct or need to jsonify <br>
