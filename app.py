import streamlit as st
import qrcode
from PIL import Image
st.title("Qr code generator")
data=st.text_input("enter url")
if st.button("Generate QR"):
if data:
  qrqrcode.make(data)
  qr.save("qr.png")
  img = Image.open("qr.png")
  with open("qr.png", "rb") as f:
    st.download_button("Download QR", f, file_name="qr.png")
else:
  st.warning("Please enter some text")
