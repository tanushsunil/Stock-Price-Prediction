import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('linear_regression.sav', 'rb'))


# creating a function for Prediction

def adherence_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The patient is not adhered'
    else:
        return 'The patient is adhered'


def main():

    # giving a title
    st.title('Patient Adherence Web App')

    # getting the input data from the user

    Age_1 = st.text_input('Age')
    Prescription_Days_1 = st.text_input('Prescription Days')
    Gender = st.selectbox('Select you Gender',
     ('Male', 'Female'))



    if Gender == 'Male':
        Male, Female = 1,0
        st.write('You selected:', Gender)
    else:
        Male, Female = 0,1
        st.write('You selected:', Gender)
    

        
    # code for Prediction
    adherence_diagnosis = ''

    # creating a button for Prediction

    if st.button('Get Adherence Test Result'):
        adherence_diagnosis = adherence_prediction(
            [Age, Prescription_Days, Male, Female])

    st.success(adherence_diagnosis)


if __name__ == '__main__':
    main()
