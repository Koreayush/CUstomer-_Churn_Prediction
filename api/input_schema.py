from pydantic import BaseModel

class ChurnInput(BaseModel):

    SeniorCitizen: str
    tenure: int
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    PaperlessBilling: str
    MonthlyCharges: float
    TotalCharges: float
    avg_monthly_spend: float
    InternetService: str
    Contract: str
    PaymentMethod: str
    