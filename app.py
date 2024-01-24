# app.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import pickle
import joblib
import pandas as pd
import io

app = FastAPI()

# Load the preprocessing pipeline and Naive Bayes model
processed = joblib.load('imp_scale')
winsor = joblib.load('winsor')
model_nb = pickle.load(open('Naive_bayes.pkl', 'rb'))

class InputData(BaseModel):
    Date: str
    Machine_ID: str
    Load_cells: float
    Hydraulic_Pressure_bar: float
    Coolant_Pressure_bar: float
    Air_System_Pressure_bar: float
    Coolant_Temperature_C: float
    Hydraulic_Oil_Temperature_C: float
    Proximity_sensors: float
    Spindle_Vibration_um: float
    Tool_Vibration_um: float
    Spindle_Speed_RPM: float
    Voltage_volts: float
    Torque: float
    Cutting_Force_kN: float

def preprocess_data(input_data, processed, winsor):
    # Replace this with your actual preprocessing logic
    # Example: assuming 'Machine_ID', 'Duration', 'Status' are columns
    # in the input_data DataFrame

    df_x = input_data.drop(['Date', 'Machine_ID'], axis = 1)
    #input_data_transformed = processed.transform(df_x)
    input_data_transformed = pd.DataFrame(processed.transform(df_x), columns = processed.get_feature_names_out()) 
    # Winsorization
    input_data_winsorized = winsor.transform(input_data_transformed)

    processed_data = input_data_winsorized.copy()  # Placeholder, replace with actual preprocessing


    return processed_data

@app.post("/predict")
async def predict_csv(file: UploadFile = File(...)):
    try:
        # Read the uploaded CSV file into a pandas DataFrame
        content = await file.read()
        input_data = pd.read_csv(io.StringIO(content.decode('utf-8')))

        # Preprocess the input data
        processed_data = preprocess_data(input_data, processed, winsor)

        # Make predictions using the loaded model
        predictions = model_nb.predict(processed_data)

        # Return the predictions
        return {"prediction": predictions.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))