import streamlit as st
from PIL import Image

# Title of the app
st.title('Streamlit App with an Image')

# Button widget
if st.button('Say hello'):
    st.write('Hello, Streamlit!')

# Slider widget
slider_value = st.slider('Select a value', 0, 100, 50)
st.write(f'Slider value: {slider_value}')

# Image with caption
image = Image.open(r"C:\Users\apoor\Downloads\kyuubi-nine-tailed-fox-ycttgiblrqeyggn0.jpg")
st.image(image, caption='This is an example image.', use_column_width=True)

