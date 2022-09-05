import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model

# loading the model
model = load_model('dog_breed.h5')

# classes
CLASS_NAMES = ['Scottish Deerhound','Maltese Dog','Bernese Mountain Dog']

# Setting title
st.title('Dog Breed Prediction')
st.markdown('Upload an image of the dog')

# uploading the dog image
dog_image = st.file_uploader('Choose an image...', type='png')
submit = st.button('Predict')

# On predict button click
if submit:
    if dog_image is not None:

        # Convert the file to an opencv image
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # display the image
        st.image(opencv_image, channels='BGR')
        # resizing the image
        opencv_image = cv2.resize(opencv_image, (224, 224))
        # convert image to 4 dimension
        opencv_image.shape = (1, 224, 224, 3)

        # Make prediction
        Y_pred = model.predict(opencv_image)

        st.title(str('The Dog Breed is ' + CLASS_NAMES[np.argmax(Y_pred)]))


