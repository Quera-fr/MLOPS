# Import des librairies uvicorn, pickle, FastAPI, File, UploadFile, BaseModel
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from functions import DataBase

import uvicorn, pickle, os, mlflow
import pandas as pd


try:
    database = DataBase()
    database.create_table('Alert', id_alert=int, date_alert=str, message_alert=str)
except:
    pass

# Crédentials d'accès à AWS
os.environ['AWS_ACCESS_KEY_ID'] = "AKIA3R62MVALHESATEYJ"
os.environ['AWS_SECRET_ACCESS_KEY'] = "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"
os.environ['ARTIFACT_STORE_URI'] = "s3://isen-mlflow/models/"


# Création des tags
tags  = [
    {
        "name": "Hello End Point",
        "description": "Hello World"
    },
    {
        "name": "Predict from local Model",
        "description": "Predict"
    },
    {
        "name": "Upload",
        "description": "Upload : csv file"
    },
    {
        "name": "Maths End Point",
        "description": "Root Square, Square, Cube, etc."
    },
    {
        "name": "Predict Model - Mlfow",
        "description": "Root Square"
    }
]

# Création de l'application
app = FastAPI(
    title="API de prédiction",
    description="API de prédiction",
    version="1.0.0",
    openapi_tags=tags
)


#mlflow.set_tracking_uri("https://isen-mlflow-fae8e0578f2f.herokuapp.com/")
#logged_model = 'runs:/ebca7a42f07f40ea9db2af0e22bc4dd0/model Bank 22'

try:loaded_model = mlflow.pyfunc.load_model(logged_model)
except:loaded_model = None


# Point de terminaison standard
@app.get("/", tags=["Hello End Point"], description="Hello World Test")
def index():
    return {"message": "Hello World!!!"}


# Point de terminaison avec paramètre
@app.get("/hello", tags=["Hello End Point"])
def hello(name: str='World'):
    return {"message": f"Hello {name}"}


# Point de terminaison avec paramètre optionnel dans l'URL
@app.get("/hello/{name}", tags=["Hello End Point"])
def hello(name):
    return {"message": f"Hello {name}"}


# Point de terminaison Post (racine carrée)
@app.post("/root_square", tags=["Maths End Point"])
def root_square(number: int):
    return {"result": number**0.5}

@app.post("/square", tags=["Maths End Point"])
def square(number: int):
    return {"result": number**2}

@app.post("/cube", tags=["Maths End Point"])
def cube(number: int):
    return {"result": number**3}


# Création du modèle de données (age, job, marital, education, default, balance, housing, loan, campaign, pdays, previous, poutcome)
class Credit(BaseModel):
    age: int
    job: int
    marital: int
    education: int
    default: int
    balance: int
    housing: int
    loan: int
    campaign: int
    pdays: int
    previous: int
    poutcome: int

# Point de terminaison : Prédiction
@app.post("/predict", tags=["Predict Model - Mlfow"])
def predict_mlflow(credit: Credit):
    try:
        predict_value = loaded_model.predict(credit.dict())[0]
        return {"pred" : str(predict_value)}
    except:
        database.add_row('Alert', date_alert='2021-09-01', message_alert='Erreur de prédiction')


# Point de terminaison : Prédiction from MLFLOW
@app.post("/predict-local", tags=["Predict from local Model"])
def predict(credit: Credit):
    with open('utiles/model.pkl', 'rb') as f: model = pickle.load(f)
    predict_value = int(model.predict(credit.dict())[0])
    return {"pred" : str(predict_value)}


# Point de terminaison qui permet de verser un fichier
@app.post("/uploadfile", tags=["Upload", "Predict from local Model"])
def create_upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)                                     # Read with pandas
    with open('utiles/model.pkl', 'rb') as f: model = pickle.load(f)
    pred = model.predict(df)                                        # Prédiction
    return {"filename": str(pred)}                                  # Retourne le nom du fichier


# Démarage de l'application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)