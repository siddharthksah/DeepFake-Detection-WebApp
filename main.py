#adding the capabilities of image URL as an input



# importing the necessary packages
import keras
import numpy as np
import streamlit as st
from PIL import Image
from skimage import transform
import requests
from io import BytesIO

hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)


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
url = ""
url = st.text_input("Or paste the image URL here", 'https://media.nature.com/lw800/magazine-assets/d41586-020-01430-5/d41586-020-01430-5_17977552.jpg')

if url != "https://media.nature.com/lw800/magazine-assets/d41586-020-01430-5/d41586-020-01430-5_17977552.jpg":
    count = count + 1



if uploaded_file is not None:

    if count == 0:

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

    else:
        pass
        # response = requests.get('https://media.nature.com/lw800/magazine-assets/d41586-020-01430-5/d41586-020-01430-5_17977552.jpg')
        # uploaded_image = Image.open(BytesIO(response.content))
        # st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)




if st.button('Real or Fake?'):

    #checking if user uploaded any file
    if count > 0 :
        #st.write("Please choose a file!")
        response = requests.get(url)
        uploaded_image = Image.open(BytesIO(response.content))
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

        st.write("Processing...")

        # preprocessing the image to use in the trained model
        np_image = uploaded_image
        np_image = np.array(np_image).astype('float32') / 255
        np_image = transform.resize(np_image, (224, 224, 3))
        np_image = np.expand_dims(np_image, axis=0)

        # loading pre trained model called model.h5, you can find the code to export this on my GitHub https://github.com/siddharthksah
        model = keras.models.load_model("model.h5")
        probab = model.predict(np_image)[0][0]
        st.write("The probability of this image being real is: ")
        st.write(probab)

        if probab < 0.001:
            st.write("which means this image is most likely fake, do not trust everything you see on the internet.")
            st.image('fake_drake.png', caption="Drake doesn't approve", use_column_width=True)

        if probab > 0.9:
            st.write(
                "which means this image is most likely real, still do not trust everything you see on the internet.")
            st.image('real_drake.jpg', caption="Drake approves", use_column_width=True)

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


st.write('\n')
st.write('\n')
st.write('\n')

st.write("""
#### Made by Siddharth """)
# st.markdown(
#     """<a href="https://www.siddharthsah.com/">siddharthsah.com</a>""", unsafe_allow_html=True,
# )
link = '[siddharthsah.com](http://www.siddharthsah.com/)'
st.markdown(link, unsafe_allow_html=True)
