import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

churn_data = pd.read_csv("F:\\Study\\Customer-Churn-Analysis-and-Classification\\tel_churn.csv")
x=churn_data.drop('Churn',axis=1)
y=churn_data['Churn']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

loaded_model = pickle.load(open('F:\\Study\\Customer-Churn-Analysis-and-Classification\\model.sav', 'rb'))

def chrun_prediction(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person will not churn'
    else:
      return 'The person will churn'

def main():

   st.title(":green[How to Use Prediction System]")
   st.subheader("Just Enter all parameters in Prediction Page and click on :blue[Churn Analysis Prediction.]")

   st.subheader("Enter Your Data")

   SeniorCitizen = st.text_input('SeniorCitizen ( If a person is SeniorCitizen Enter = 1 | else Enter = 0 )')
   MonthlyCharges = st.text_input('MonthlyCharges ( Enter your Monthy Charges rate )')
   TotalCharges = st.text_input('TotalCharges ( Enter your Total Charges rate )')
   gender_Female = st.text_input('gender_Female ( If a person is Female Enter = 1 | else Enter = 0 )')
   gender_Male = st.text_input('gender_Male ( If a person is Male Enter = 1 | else Enter = 0 )')
   Partner_No = st.text_input('Partner_No ( If There is No Partner Enter = 1 | else Enter = 0 )')
   Partner_Yes = st.text_input('Partner_Yes ( If There is Any Partner Enter = 1 | else Enter = 0 )')
   Dependents_No = st.text_input('Dependents_No ( If There is No Dependents Enter = 1 | else Enter = 0 )')
   Dependents_Yes = st.text_input('Dependents_Yes ( If There is Any Dependents Enter = 1 | else Enter = 0 )')
   PhoneService_No = st.text_input('PhoneService_No ( If There is No Phone Service Enter = 1 | else Enter = 0 )')
   PhoneService_Yes = st.text_input('PhoneService_Yes ( If There is Any Phone Service Enter = 1 | else Enter = 0 )')
   MultipleLines_No = st.text_input('MultipleLines_No ( If There is No Multiple Lines Enter = 1 | else Enter = 0 )')
   MultipleLines_No_phone_service = st.text_input('MultipleLines_No phone service ( If There is No Phone Service Multiple Lines Enter = 1 | else Enter = 0 )')
   MultipleLines_Yes = st.text_input('MultipleLines_Yes ( If There is Any Multiple Lines Enter = 1 | else Enter = 0 )')
   InternetService_DSL = st.text_input('InternetService_DSL ( If Internet Service is DSL Enter = 1 | else Enter = 0 )')
   InternetService_Fiber_optic = st.text_input('InternetService_Fiber optic ( If Internet Service is Fiber Optic Enter = 1 | else Enter = 0 )')
   InternetService_No = st.text_input('InternetService_No ( If There is No Internet Service Enter = 1 | else Enter = 0 )')
   OnlineSecurity_No = st.text_input('OnlineSecurity_No ( If There is No Online Security Enter = 1 | else Enter = 0 )')
   OnlineSecurity_No_internet_service = st.text_input('OnlineSecurity_No internet service ( If There is No Internet Service Online Security Enter = 1 | else Enter = 0 )')
   OnlineSecurity_Yes = st.text_input('OnlineSecurity_Yes ( If There is Any Online Security Enter = 1 | else Enter = 0 )')
   OnlineBackup_No = st.text_input('OnlineBackup_No ( If There is No Online Backup Enter = 1 | else Enter = 0 )')
   OnlineBackup_No_internet_service = st.text_input('OnlineBackup_No internet service ( If There is No Internet Service Online Backup Enter = 1 | else Enter = 0 )')
   OnlineBackup_Yes = st.text_input('OnlineBackup_Yes ( If There is Any Online Backup Enter = 1 | else Enter = 0 )')
   DeviceProtection_No = st.text_input('DeviceProtection_No ( If there is No Device Protection Enter = 1 | else Enter = 0 )')
   DeviceProtection_No_internet_service = st.text_input('DeviceProtection_No internet service ( If There is No Internet Service Device Protection Enter = 1 | else Enter = 0 )')
   DeviceProtection_Yes = st.text_input('DeviceProtection_Yes ( If There is Any Device Protection Enter = 1 | else Enter = 0 )')
   TechSupport_No = st.text_input('TechSupport_No ( If There is No Tech Support Enter = 1 | else Enter = 0 )')
   TechSupport_No_internet_service = st.text_input('TechSupport_No internet service ( If There is No Internet Service Tech Support Enter = 1 | else Enter = 0 )')
   TechSupport_Yes = st.text_input('TechSupport_Yes ( If There is Any Tech Support Enter = 1 | else Enter = 0 )')
   StreamingTV_No = st.text_input('StreamingTV_No ( If There is No SteamingTV Enter = 1 | else Enter = 0 )')
   StreamingTV_No_internet_service = st.text_input('StreamingTV_No internet service ( If There is No Internet Service StreamingTV Enter = 1 | else Enter = 0 )')
   StreamingTV_Yes = st.text_input('StreamingTV_Yes ( If There is Any StreamingTV Enter = 1 | else Enter = 0 )')
   StreamingMovies_No = st.text_input('StreamingMovies_No ( If There is No Streaming Movies Enter = 1 | else Enter = 0 )')
   StreamingMovies_No_internet_service = st.text_input('StreamingMovies_No internet service ( If There is No Internet Service Streaming Movies Enter = 1 | else Enter = 0 )')
   StreamingMovies_Yes = st.text_input('StreamingMovies_Yes ( If There is Any Streaming Movies Enter = 1 | else Enter = 0 )')
   Contract_Month_to_month = st.text_input('Contract_Month-to-month ( If There is Any Month-To_Month Contract Enter = 1 | else Enter = 0 )')
   Contract_One_year = st.text_input('Contract_One year ( If There is Any One Year Contract Enter = 1 | else Enter = 0 )')
   Contract_Two_year = st.text_input('Contract_Two year ( If There is Any Two Year Contract Enter = 1 | else Enter = 0 )')
   PaperlessBilling_No = st.text_input('PaperlessBilling_No ( If There is No Paperless Billing Enter = 1 | else Enter = 0 )')
   PaperlessBilling_Yes = st.text_input('PaperlessBilling_Yes ( If There is Any Paperless Billing Enter = 1 | else Enter = 0 )')
   PaymentMethod_Bank_transfer_automatic = st.text_input('PaymentMethod_Bank transfer (automatic) ( If a Person Use Any Automatic Bank_Transfer Payment Method Enter = 1 | else Enter = 0 )')
   PaymentMethod_Credit_card_automatic = st.text_input('PaymentMethod_Credit card (automatic) ( If a Person Use Any Automatic Credit_Card Payment Method Enter = 1 | else Enter = 0 )')
   PaymentMethod_Electronic_check = st.text_input('PaymentMethod_Electronic check ( If a Person Use Any Automatic Electronic_Check Payment Method Enter = 1 | else Enter = 0 )')
   PaymentMethod_Mailed_check = st.text_input('PaymentMethod_Mailed check ( If a Person Use Any Automatic Mailed_Check Payment Method Enter = 1 | else Enter = 0 )')
   tenure_group_1_12 = st.text_input('tenure_group_1 - 12 ( If a Person"s Tenure is Between 1 to 12  Enter = 1 | else Enter = 0 )')
   tenure_group_13_24 = st.text_input('tenure_group_13 - 24 ( If a Person"s Tenure is Between 13 to 24 Enter = 1 | else Enter = 0 )')
   tenure_group_25_36 = st.text_input('tenure_group_25 - 36 ( If a Person"s Tenure is Between 25 to 36 Enter = 1 | else Enter = 0 )')
   tenure_group_37_48 = st.text_input('tenure_group_37 - 48 ( If a Person"s Tenure is Between 37 to 48 Enter = 1 | else Enter = 0 )')
   tenure_group_49_60 = st.text_input('tenure_group_49 - 60 ( If a Person"s Tenure is Between 49 to 60 Enter = 1 | else Enter = 0 )')
   tenure_group_61_72 = st.text_input('tenure_group_61 - 72 ( If a Person"s Tenure is Between 61 to 72 Enter = 1 | else Enter = 0 )')

   predict = ''

   if st.button('Churn Analysis Prediction'):
        predict = chrun_prediction([SeniorCitizen,MonthlyCharges,TotalCharges,gender_Female,gender_Male,Partner_No,Partner_Yes,Dependents_No,Dependents_Yes,PhoneService_No,PhoneService_Yes,MultipleLines_No,MultipleLines_No_phone_service,MultipleLines_Yes,InternetService_DSL,InternetService_Fiber_optic,InternetService_No,OnlineSecurity_No,OnlineSecurity_No_internet_service,OnlineSecurity_Yes,OnlineBackup_No,OnlineBackup_No_internet_service,OnlineBackup_Yes,DeviceProtection_No,DeviceProtection_No_internet_service,DeviceProtection_Yes,TechSupport_No,TechSupport_No_internet_service,TechSupport_Yes,StreamingTV_No,StreamingTV_No_internet_service,StreamingTV_Yes,StreamingMovies_No,StreamingMovies_No_internet_service,StreamingMovies_Yes,Contract_Month_to_month,Contract_One_year,Contract_Two_year,PaperlessBilling_No,PaperlessBilling_Yes,PaymentMethod_Bank_transfer_automatic,PaymentMethod_Credit_card_automatic,PaymentMethod_Electronic_check,PaymentMethod_Mailed_check,tenure_group_1_12,tenure_group_13_24,tenure_group_25_36,tenure_group_37_48,tenure_group_49_60,tenure_group_61_72])

   st.success(predict)

if __name__ == '__main__':
    main()