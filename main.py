import pickle
import streamlit as st
import requests
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

st.title("Pima Indians Diabetes Prediction")
st.text('Made by Hrishikesh Kini')
st.header('Enter The Values')
model = pickle.load(open('svc.pkl','rb'))
ss = pickle.load(open('standardscaler.pkl','rb'))
v1 = st.text_input("Pregnancies")
v2 = st.text_input("Glucose")
v3 = st.text_input("Blood Pressure")
v4 = st.text_input("Skin Thickness")
v5 = st.text_input("Insulin")
v6 = st.text_input("BMI")
v7 = st.text_input("Age")
prediction = 2
if st.button('Check Result'):
    data = []
    data.append(int(v1))
    data.append(int(v2))
    data.append(int(v3))
    data.append(int(v4))
    data.append(int(v5))
    data.append(int(v6))
    data.append(int(v7))
    data = np.array(data).reshape(1,-1)
    data = ss.transform(data)
    prediction = model.predict(data)
if prediction == 1:
    original_title = '<h3 style="color:Red; font-size: 50px">Result Positive</h3>'
    st.markdown(original_title, unsafe_allow_html=True)
elif prediction == 0:
    original_title = '<h3 style="color:Green; font-size: 50px">Result Negative</h3>'
    st.markdown(original_title, unsafe_allow_html=True)
else:
    st.header('Enter values for prediction')
