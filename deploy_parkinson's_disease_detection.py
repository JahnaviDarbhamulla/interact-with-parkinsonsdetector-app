# -*- coding: utf-8 -*-
"""Deploy_Parkinson's_Disease_Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J5VFzugRTJv-1Ygcq4UwYdZaX34pImZT

#**Parkinson's Disease Detection using Support Vector Machines.**

###**Importing the Dependencies**
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

"""###**Data Collection & Analysis**"""

# loading the data from csv file to a Pandas DataFrame
parkinsons_data = pd.read_csv('/content/parkinsons.csv', encoding = 'unicode_escape')

# printing the first 5 rows of the dataframe
parkinsons_data.head()

# number of rows and columns in the dataframe
parkinsons_data.shape

# getting more information about the dataset
parkinsons_data.info()

# checking for missing values in each column
parkinsons_data.isnull().sum()

# getting some statistical measures about the data
parkinsons_data.describe()

# distribution of target Variable
parkinsons_data['status'].value_counts()

"""**1  --> Parkinson's Positive**

**0 --> Healthy**

"""

# grouping the data bas3ed on the target variable
parkinsons_data.groupby('status').mean()

"""###**Data Pre-Processing**

####**Splitting into Dependancy and Target Variables**
"""

X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']

print(X)

print(Y)

"""####**Splitting the data to training data & Test data**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""####**Data Standardization**"""

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_train)

"""###**Model Training**

####**Support Vector Machine Model**
"""

model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

"""###**Model Evaluation**

####**Accuracy Score**
"""

# accuracy score on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print('Accuracy score of training data : ', training_data_accuracy)

# accuracy score on training data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print('Accuracy score of test data : ', test_data_accuracy)

"""####**Building a Predictive System**"""

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

# changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the data
std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")

import pickle
pickle.dump(model,open('saved.pkl','wb')) #saving our model in .pkl file
model1 = pickle.load(open('saved.pkl'))

!pip install streamlit

!pip install pyngrok==4.1.1

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# # imports
# import numpy as np
# import pandas as pd
# import streamlit as st
# import pickle
# from PIL import Image
# image = Image.open('/content/parkinson.jpeg')
# 
# 
# 
# model = pickle.load(open('/content/parkinsons_model.sav','rb'))
# 
# # creating a function for prediction
# def disease_prediction(input_data):
# 	input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)
# 
# 	# changing input data to a numpy array
# 	input_data_as_numpy_array = np.asarray(input_data)
# 
# 	# reshape the numpy array
# 	input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# 
# 
# 	prediction = model.predict(input_data_reshaped)
# 	print(prediction)
# 
# 
# 	if (prediction[0] == 0):
# 		return "The Person does not have Parkinsons Disease"
# 
# 	else:
# 		return "The Person has Parkinsons"
# 
# 
# def main():
# 
# 	st.set_page_config(
#     page_title="Parkinsons disease",
#     page_icon="????",
#     layout="wide",
#     initial_sidebar_state="expanded"
# 	)
# 
# 	# Title
# 	st.title("Parkinson's Disease Detection")
# 	st.subheader("What is Parkinson's Disease ?")
# 	st.write("Parkinsons disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.")
# 	st.subheader("About the Dataset")
# 	st.write("This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease.Each column in the table is a particular voice measure, and each row corresponds one of 195 voice recording from the individuals .The main aim of the data is to discriminate healthy people from those with PD, according to status column which is set to 0 for healthy and 1 for PD.")
# 	st.image(image, caption='Parkinsons Disease')
# 	# Input data
# 	# MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	...	MDVP:APQ	Shimmer:DDA	NHR	HNR	RPDE	DFA	spread1	spread2	D2	PPE
# 	st.subheader("Let's test it out")
# 	col1, col2, col3, col4, col5= st.columns(5)
# 	
# 
# 	col1.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Vocal fundamental frequency"}</h1>', unsafe_allow_html=True)
# 	MDVPFoHz = col1.text_input("Average vocal fundamental frequency")
# 	MDVPFhiHz = col1.text_input("Maximum vocal fundamental frequency")
# 	MDVPFloHz = col1.text_input("Minimum vocal fundamental frequency")
# 
# 	col2.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Several measures of variation in fundamental frequency"}</h1>', unsafe_allow_html=True)
# 	MDVPJitter = col2.text_input("MDVP:Jitter(%)")	
# 	MDVPJitterAbs	= col2.text_input("MDVP:Jitter(Abs)")
# 	MDVPRAP	= col2.text_input("MDVP:RAP")
# 	MDVPPPQ	= col2.text_input("MDVP:PPQ")
# 	JitterDDP = col2.text_input("Jitter:DDP")
# 
# 	col3.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Several measures of variation in amplitude"}</h1>', unsafe_allow_html=True)
# 	MDVPShimmer = col3.text_input("MDVP:Shimmer")
# 	MDVPShimmerdB = col3.text_input("MDVP:Shimmer(dB)")
# 	ShimmerAPQ3 = col3.text_input("Shimmer:APQ3")
# 	ShimmerAPQ5 = col3.text_input("Shimmer:APQ5")
# 	MDVPAPQ = col3.text_input("MDVP:APQ")
# 	ShimmerDDA = col3.text_input("Shimmer:DDA")
# 	
# 	col4.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Two nonlinear dynamical complexity measures"}</h1>', unsafe_allow_html=True)
# 	RPDE = col4.text_input("RPDE")
# 	D2 = col4.text_input("D2")
# 	DFA = col4.text_input("Signal fractal scaling exponent")
# 
# 	col5.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Three nonlinear measures of fundamental frequency variation"}</h1>', unsafe_allow_html=True)
# 	spread1 = col5.text_input("spread1")
# 	spread2 = col5.text_input("spread2")
# 	PPE = col5.text_input("PPE")
# 
# 	# code for prediction
# 	diagnosis = ' '
# 
# 	if st.button("Parkinsons Disease Result"):
# 		diagnosis = disease_prediction([MDVPFoHz,MDVPFhiHz,MDVPFloHz,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,RPDE,D2,DFA,spread1,spread2,PPE])
# 
# 	st.success(diagnosis)
# 
# if __name__ == '__main__':
# 	main()

!ls

!ngrok authtoken xxxx

!ngrok

from pyngrok import ngrok

# !nohub streamlit run app.py 
!streamlit run app.py&>/dev/null&

!pgrep streamlit

# Setup a tunnel to the streamlit port 8501
public_url = ngrok.connect(port='8501')
public_url
