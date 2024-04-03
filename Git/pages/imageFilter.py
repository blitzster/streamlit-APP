import cv2
import numpy as np
import streamlit as st
from PIL import Image

def apply_filters(image, filter_option):
    if filter_option == "Original Image":
        return image
    elif filter_option == "Grayscale":
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grayscale_image
    elif filter_option == "Blur":
        blurred_image = cv2.GaussianBlur(image, (7, 7), 0)
        return blurred_image
    elif filter_option == "Edge Detection":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edge_image = cv2.Canny(gray, 100, 200)
        return edge_image

def main():
    st.title("Image Processing and Filtering")

    # Sidebar
    st.sidebar.header("Choose an Option")
    filter_option = st.sidebar.selectbox(
        "Filter",
        ["Original Image", "Grayscale", "Blur", "Edge Detection"]
    )

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read image from file uploader
        pil_image = Image.open(uploaded_file)
        image = np.array(pil_image)

        # Apply selected filter
        filtered_image = apply_filters(image, filter_option)

        # Display filtered image
        st.image(filtered_image, caption=filter_option, use_column_width=True)

if __name__ == "__main__":
    main()
