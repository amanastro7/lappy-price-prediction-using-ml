###########################################
############## IMPORTS ####################
###########################################

import streamlit as st
import pickle
import numpy as np

###########################################
############ IMPORTING MODELS #############
###########################################

pipe = pickle.load(open('pipe.pkl', 'rb'))
laptop = pickle.load(open('laptop.pkl', 'rb'))


###########################################
############## STREAMLIT ##################
###########################################

st.title('PRICE💰 PREDICTION OF LAPTOPS👨‍💻 USING ML🤖')
st.image('laptops.jpeg')

# Brand Of The Laptop
company = st.selectbox('BRAND💻', laptop['Company'].unique())


col1, col2, col3 = st.columns(3)

with col1:
    # Type Of Laptop
    type = st.selectbox('TYPE', laptop['TypeName'].unique())
with col2:
    # Ram Of The Laptop
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
with col3:
    # Weight Of The Laptop
    weight = st.number_input('WEIGHT (kg)')



col4, col5, col6 = st.columns(3)

with col4:
    # Touchscreen
    touchscreen = st.selectbox('TOUCHSCREEN', ['NO', 'YES'])
with col5:
    # IPS
    ips = st.selectbox('IPS', ['NO', 'YES'])
with col6:
    # Screen Size
    screen_size = st.number_input('SCREEN SIZE')




col7, col8, col9 = st.columns(3)

with col7:
    # Resolution
    resolution = st.selectbox('SCREEN RESOLUTION', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
with col8:
    # CPU
    cpu = st.selectbox('CPU BRAND', laptop['CPU'].unique())
with col9:
    # HDD
    hdd = st.selectbox('HDD (GB)', [0, 8, 128, 256, 512, 1024, 2048])




col10, col11, col12 = st.columns(3)

with col10:
    # SSD
    ssd = st.selectbox('SSD (GB)', [0, 8, 128, 256, 512, 1024])
with col11:
    # GPU
    gpu = st.selectbox('GPU BRAND', laptop['GPU'].unique())
with col12:
    # Operating System
    os = st.selectbox('OS', laptop['OS'].unique())



###########################################
############### RESULT ####################
###########################################

if st.button('PREDICT PRICE💵'):

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0


    X_resolution = int(resolution.split('x')[0])
    Y_resolution = int(resolution.split('x')[1])
    ppi = (((X_resolution**2) + (Y_resolution**2))**0.5) / screen_size

    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)
    result = pipe.predict(query)
    result = np.exp(result)
    result = result[0]
    st.subheader('THE PREDICTED PRICE💰 OF THE LAPTOP👨‍💻 IS : ₹ ' + str(int(result)) + '.')
    st.image('laptop_end.jpg')