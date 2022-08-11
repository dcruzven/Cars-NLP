# Imports
import streamlit as st
import pandas as pd
import pickle
import xgboost as xgb

#Title
st.write("# Used Car Price Range Predictions")

#loading df
df = pd.read_csv('data/CleanData3bins.csv')
df = df.drop(columns=['Unnamed: 0', 'SalePrice', 'PriceCategory', 'CleanReviews'])

#Picking the Drive Train
driveTrain = st.selectbox(
    label='Select the drivetrain of the car.', 
    options=df['DriveTrain'].value_counts().index)

#Picking the mileage
mileage = st.number_input(
    label='Enter the mileage of the car.')

#Picking the year
year = st.number_input(
    label='Enter the year of the car.')

#Picking the engine sizecon
engineSize = st.number_input(
    label='Enter the engine size (Ex. 3.5).')

#Picking cylinders
cylinders = st.number_input(
    label='Enter the number of cylinders.')

#Picking make
make = st.selectbox(
    label='Select the make of the car.', 
    options=df['newMake'].value_counts().index)

#Picking mpg
mpg = st.number_input(
    label='Enter the mpg.')

row =[driveTrain, mileage, year, engineSize, cylinders, make, mpg]
columns = df.columns
user_car = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Now predicting!
if st.button(label="Click to Predict Price Range"):

    # Load the model
    model = pickle.load(open('xgb_model.sav', 'rb'))
    # Make predictions (and get out pred probabilities)
    pred = model.predict(user_car)[0]
    proba = model.predict_proba(user_car)[:,1][0]

    if pred == 'Cheap':
        st.write('# Estimated price range is 0-28k$')
        st.write(f"## Predicted probability for price to be in that range: {proba*100:.2f}")

    elif pred == 'Average':
        st.write('# Estimated price range is 28k$-45k$')
        st.write(f"## Predicted probability for price to be in that range: {proba*100:.2f}")
    else:
        st.write('# Estimated price range is 45k$+')
        st.write(f"## Predicted probability for price to be in that range: {proba*100:.2f}")