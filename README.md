                                         Optimization of Machine Downtime

Unplanned machine downtime led to loss of productivity for one of the leading vehicle fuel pump manufacturers

Objective:

Minimize the unplanned  machine downtime by minimizing maintenance cost and maximizing equipment efficiency

Dataset:

- Date

- Machine_ID 

- Load cells  

- Hydraulic_Pressure(bar)

- Coolant_Pressure(bar) 

- Air_System_Pressure(bar) 

- Coolant_Temperature(°C) 

- Hydraulic_Oil_Temperature(°C)

- Proximity sensors 

- Spindle_Vibration(µm)

- Cutting_Tool_Vibration(µm) 

- Spindle _Speed(RPM) 

- Current (volts) 

- Torque(Nm) 

- Cutting_force(N) 

- Downtime

Pre-processing:

- Null imputation with mean
  
- Standardization using minmax() scaler
  
- Removing outliers using Winsorizer
  
- Oversampling using SMOTE technique

Model: 

- Naive Bayes

Deployment:

- FastAPI

Monitoring:

- Evidently
  
- Reports were generated for Data Stability, Data drift in columns considering column ‘Torque’, Data Drift in dataset, Data quality and Data integrity in dataset






