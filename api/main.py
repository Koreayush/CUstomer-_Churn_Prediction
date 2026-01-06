from fastapi import FastAPI
import uvicorn
import joblib
from input_schema import ChurnInput
from logic import prepare_input

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts whether a customer will churn",
    version="1.0"
)
## Importing the files  

model_package = joblib.load("churn_model.joblib")
model = model_package["model"]
feature_columns = model_package["features"]

## Create a post function to get the data from user and give them result back 

@app.post("/predict")
def predict_churn(data: ChurnInput):
    df = prepare_input(data, feature_columns)

    prediction = int(model.predict(df)[0])
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "N0",
        "churn_probability": round(probability * 100, 2) 
    }


@app.get("/")
async def root():
    return {"status": "Hellow , I am alive"}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
