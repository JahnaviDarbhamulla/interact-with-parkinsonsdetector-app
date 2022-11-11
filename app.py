# imports
import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
image = Image.open('parkinson.jpeg')



model = pickle.load(open('parkinsons_model.sav','rb'))

# creating a function for prediction
def disease_prediction(input_data):
	input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

	# changing input data to a numpy array
	input_data_as_numpy_array = np.asarray(input_data)

	# reshape the numpy array
	input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


	prediction = model.predict(input_data_reshaped)
	print(prediction)


	if (prediction[0] == 0):
		return "The Person does not have Parkinsons Disease"

	else:
		return "The Person has Parkinsons"


def main():

	st.set_page_config(
    page_title="Parkinsons disease",
    page_icon="🧊",
    initial_sidebar_state="expanded"
	)

	# Title
	st.title("Parkinson's Disease Detection")
	st.subheader("What is Parkinson's Disease ?")
	st.write("Parkinsons disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.")
	st.subheader("About the Dataset")
	st.write("This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease.Each column in the table is a particular voice measure, and each row corresponds one of 195 voice recording from the individuals .The main aim of the data is to discriminate healthy people from those with PD, according to status column which is set to 0 for healthy and 1 for PD.")
	st.image(image, caption='Parkinsons Disease')
	# Input data
	# MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	...	MDVP:APQ	Shimmer:DDA	NHR	HNR	RPDE	DFA	spread1	spread2	D2	PPE
	st.subheader("Let's test it out")
	col1, col2, col3, col4, col5= st.columns(5)
	

	col1.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Vocal fundamental frequency"}</h1>', unsafe_allow_html=True)
	MDVPFoHz = col1.text_input("Average vocal fundamental frequency")
	MDVPFhiHz = col1.text_input("Maximum vocal fundamental frequency")
	MDVPFloHz = col1.text_input("Minimum vocal fundamental frequency")

	col2.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Several measures of variation in fundamental frequency"}</h1>', unsafe_allow_html=True)
	MDVPJitter = col2.text_input("MDVP:Jitter(%)")	
	MDVPJitterAbs	= col2.text_input("MDVP:Jitter(Abs)")
	MDVPRAP	= col2.text_input("MDVP:RAP")
	MDVPPPQ	= col2.text_input("MDVP:PPQ")
	JitterDDP = col2.text_input("Jitter:DDP")

	col3.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Several measures of variation in amplitude"}</h1>', unsafe_allow_html=True)
	MDVPShimmer = col3.text_input("MDVP:Shimmer")
	MDVPShimmerdB = col3.text_input("MDVP:Shimmer(dB)")
	ShimmerAPQ3 = col3.text_input("Shimmer:APQ3")
	ShimmerAPQ5 = col3.text_input("Shimmer:APQ5")
	MDVPAPQ = col3.text_input("MDVP:APQ")
	ShimmerDDA = col3.text_input("Shimmer:DDA")
	
	col4.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Two nonlinear dynamical complexity measures"}</h1>', unsafe_allow_html=True)
	RPDE = col4.text_input("RPDE")
	D2 = col4.text_input("D2")
	DFA = col4.text_input("Signal fractal scaling exponent")

	col5.write(f'<h1 style="color:#9F73AB;font-size:14px;">{"Three nonlinear measures of fundamental frequency variation"}</h1>', unsafe_allow_html=True)
	spread1 = col5.text_input("spread1")
	spread2 = col5.text_input("spread2")
	PPE = col5.text_input("PPE")

	# code for prediction
	diagnosis = ' '

	if st.button("Parkinsons Disease Result"):
		diagnosis = disease_prediction([MDVPFoHz,MDVPFhiHz,MDVPFloHz,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,RPDE,D2,DFA,spread1,spread2,PPE])

	st.success(diagnosis)

if __name__ == '__main__':
	main()
