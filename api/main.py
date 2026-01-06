from fastapi import FastAPI , Request ,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses  import HTMLResponse
import uvicorn
import joblib
from input_schema import ChurnInput
from logic import prepare_input


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts whether a customer will churn",
    version="1.0"
)

templates = Jinja2Templates(directory="Templates")

## Loding Model Files 

model_package = joblib.load("churn_model.joblib")
model = model_package["model"]
feature_columns = model_package["features"]


## Home Page 

@app.get("/" , response_class=HTMLResponse)
def home(request : Request):
    return templates.TemplateResponse("Home.html" , {"request" : request})


## Create a post function to get the data from user and give them result back 

@app.post("/predict", response_class=HTMLResponse)
def predict_churn(
    request: Request,

    SeniorCitizen: str = Form(...),
    tenure: int = Form(...),
    OnlineSecurity: str = Form(...),
    OnlineBackup: str = Form(...),
    DeviceProtection: str = Form(...),
    TechSupport: str = Form(...),  
    PaperlessBilling: str = Form(...),
    MonthlyCharges: float = Form(...),
    TotalCharges: float = Form(...),
    avg_monthly_spend: float = Form(...),
    InternetService: str = Form(...),
    Contract: str = Form(...),
    PaymentMethod: str = Form(...)
):
    # Convert form data → Pydantic model
    data = ChurnInput(
        SeniorCitizen=SeniorCitizen,
        tenure=tenure,
        OnlineSecurity=OnlineSecurity,
        OnlineBackup=OnlineBackup,
        DeviceProtection=DeviceProtection,
        TechSupport=TechSupport,
        PaperlessBilling=PaperlessBilling,
        MonthlyCharges=MonthlyCharges,
        TotalCharges=TotalCharges,
        avg_monthly_spend=avg_monthly_spend,
        InternetService=InternetService,
        Contract=Contract,
        PaymentMethod=PaymentMethod
    )

    df = prepare_input(data, feature_columns)

    prediction = int(model.predict(df)[0])
    probability = model.predict_proba(df)[0][1]
    
    
    if prediction == 0:
        result_text = "The customer is not likely to churn."
    else:
        result_text = "The customer is likely to churn."

    if probability < 0.4:
        risk_text = "low risk"
    elif probability < 0.7:
        risk_text = "moderate risk"
    else:
        risk_text = "high risk"

    return templates.TemplateResponse(
        "Home.html",
        {
            "request": request,
            "result_text": result_text,
            "churn_probability": round(probability * 100, 2),
            "risk_text": risk_text
        }
    )


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
