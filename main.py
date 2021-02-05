# importing the necessary packages
import keras
import numpy as np
import streamlit as st
from PIL import Image
from skimage import transform

#showing header image
st.image('./header.jpg', use_column_width=True)


#introduction of the app
st.write("""
## DeepFake Image Detector
""")

#using this count as a failsafe if the user does not upload the file and still clicks the "process image" button
count = 0

#upload button for the input image
uploaded_file = st.file_uploader("Choose the image, please make sure the image is in the correct orientation", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:

    #getting the file extension of the uploaded file
    file_name = uploaded_file.name
    extension = file_name.split(".")[1]

    if extension == "png" or  extension == "PNG":
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    elif extension == "jpeg" or extension == "JPEG":
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    elif extension == "jpg" or extension == "JPG":
        # SHOW IMAGE IF JPG FORMAT
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    else:
        st.write("Please upload .JPG , .JPEG OR .PNG format file only!")

    count = count + 1




if st.button('Process Image'):

    #checking if user uploaded any file
    if count == 0 :
        st.write("Please choose a file!")

    else:

        if extension == 'jpg' or extension == 'JPG':

            st.write("Processing...")

            #preprocessing the image to use in the trained model
            np_image = uploaded_image
            np_image = np.array(np_image).astype('float32') / 255
            np_image = transform.resize(np_image, (224, 224, 3))
            np_image = np.expand_dims(np_image, axis=0)

            #loading pre trained model called model.h5, you can find the code to export this on my GitHub https://github.com/siddharthksah
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


        if extension == 'jpeg' or extension == 'JPEG':

            st.write("Processing...")

            #preprocessing the image to use in the trained model
            np_image = uploaded_image
            np_image = np.array(np_image).astype('float32') / 255
            np_image = transform.resize(np_image, (224, 224, 3))
            np_image = np.expand_dims(np_image, axis=0)

            #loading pre trained model called model.h5, you can find the code to export this on my GitHub https://github.com/siddharthksah
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



        elif extension == 'png' or extension == 'PNG':
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
