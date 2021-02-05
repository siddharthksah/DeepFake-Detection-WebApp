# importing the necessary packages
import cv2
import keras
import numpy as np
import streamlit as st
from PIL import Image
from skimage import transform

st.image('./header.jpg', use_column_width=True)


#introduction of the app
st.write("""
## DeepFake Image Detector
""")

uploaded_file = st.file_uploader("Choose the image", type=['jpg', 'png'])

if uploaded_file is not None:

    file_name = uploaded_file.name
    extension = file_name.split(".")[1]

    if extension == "png":

        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    elif extension == "jpg":
        # SHOW IMAGE IF JPG FORMAT
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    else:
        st.write("Please upload .JPG OR .PNG format file only!")

if st.button('Process Images'):

    if extension == 'jpg':

        st.write("Processing...")

        np_image = uploaded_image
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (224, 224, 3))
        np_image = np.expand_dims(np_image, axis=0)

        model = keras.models.load_model("model.h5")
        probab = model.predict(np_image)[0][0]
        st.write("The probability of this image being real is: ")
        st.write(probab)

        if probab < 0.001 :
            st.write("which means this image is most likely fake, do not trust everything you see on the internet.")
            st.image('fake_drake.png', caption="Drake doesn't approve", use_column_width=True)

        if probab > 0.9 :
            st.write("which means this image is most likely real, still do not trust everything you see on the internet.")
            st.image('real_drake.jpg', caption="Drake approves", use_column_width=True)


    elif extension == 'png':
        st.write("Processing...")

        np_image = uploaded_image
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (224, 224, 3))
        np_image = np.expand_dims(np_image, axis=0)

        model = keras.models.load_model("model.h5")
        probab = model.predict(np_image)[0][0]
        st.write("The probability of this image being real is: ")
        st.write(probab)

        if probab < 0.001:
            st.write("which means this image is most likely fake, do not trust everything you see on the internet.")
            st.image('fake_drake.png', caption="Drake doesn't approve", use_column_width=True)

        if probab > 0.9 :
            st.write("which means this image is most likely real, still do not trust everything you see on the internet.")
            st.image('real_drake.jpg', caption="Drake approves", use_column_width=True)