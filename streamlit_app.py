import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('linear_regression.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):

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

##
def main():

    # giving a title
    st.title('Patient Adherence Web App')

    # getting the input data from the user

    Age = st.text_input('Age')
    Prescription_Days = st.text_input('Prescription Days')
    Male = st.text_input('Male')
    Female = st.text_input('Female')

    # code for Prediction
    adherence_diagnosis = ''

    # creating a button for Prediction

    if st.button('Get Adherence Test Result'):
        adherence_diagnosis = diabetes_prediction(
            [Age, Prescription_Days, Male, Female])

    st.success(adherence_diagnosis)


if __name__ == '__main__':
    main()
