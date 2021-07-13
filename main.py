import streamlit as st
import pickle
import pandas as pd
from datetime import date

model = pickle.load(open('rfcarprice.sav', 'rb'))




def main():
    current_year = date.today()
    st.title('Find the approximate Selling Price of your Car!')


    Name=st.text_input('Enter Name & Model of the Car: ')
    Present_Price=st.number_input('Present ShowRoom Price of the Car(In Lakhs): ')
    Kms_Driven=st.number_input('Kilometers the Car has been driven: ')
    Owner=st.selectbox('No Of Owner The Car has had: ',[0,1,3])
    Year=st.date_input('Enter Year it was bought: ')
    YearOld=current_year.year - Year.year
    st.write('The Car is approximately ',YearOld,'years old')


    Fuel_Type = st.selectbox('Fuel Type: ',['Petrol','Diesel','CNG'])
    if Fuel_Type=='Petrol':
        Fuel_Type=0

    elif Fuel_Type=='Diesel':
        Fuel_Type='1'

    else:
        Fuel_Type='3'

    Seller_Type = st.selectbox('Seller is Individual or Dealer?:',['Individual','Dealer'])
    if Seller_Type=='Dealer':
        Seller_Type=0
    else:
        Seller_Type=1

    Transmission_Manual = st.selectbox('Transmission?:',['Automatic','Manual'])
    if Transmission_Manual=='Automatic':
        Transmission_Manual=0
    else:
        Transmission_Manual=1


    result=''
    if st.button("Predict"):
        result =model.predict([[Present_Price, Fuel_Type,Transmission_Manual,Seller_Type,Kms_Driven,Owner,YearOld]])
    st.success('The Selling Price of your Car should be approxmately: {} Lakhs'.format(result))


if __name__=='__main__':
    main()












