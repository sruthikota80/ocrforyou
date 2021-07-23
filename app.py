import streamlit as st
import pytesseract
import cv2
from PIL import Image
st.title("OCR - Optical Character Recognition")
img = st.sidebar.file_uploader("Choose an image")
if img is not None:
  img_read = Image.open(img)
  st.image(img,caption='Uploaded Image')
  if st.button('PREDICT'):
    img_read = cv2.imread(img_read,0)
    op = pytesseract.image_to_string(img_read)
    st.write(op)
