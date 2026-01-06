import pandas as pd

def prepare_input(data, feature_columns):
    df = pd.DataFrame([data.dict()])


    yes_no_cols = [
        "SeniorCitizen",
        "OnlineSecurity",
        "OnlineBackup" ,
        "DeviceProtection",
        "TechSupport"  ,
        "PaperlessBilling",
    ]
    for  cols in yes_no_cols:
        if cols in df.columns :
            df[cols] = df[cols].map({"Yes" : 1 ,"No" : 0})

    categorical_cols = [
        "InternetService",
        "Contract",
        "PaymentMethod"
    ]

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

  
    df = df[feature_columns]

    return df
