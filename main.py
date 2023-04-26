# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:02:03 2023

@author: RASA
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

st.title("Image Pixel Value Histogram")

# Upload image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Convert image to grayscale
    image = image.convert('L')
    pixels = np.array(image.getdata())

    # Plot histogram
    fig, ax = plt.subplots()
    ax.hist(pixels, bins=256, range=[0, 256])
    ax.set_xlabel('Pixel value')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
