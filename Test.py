import json
import streamlit as st 
from streamlit_lottie import st_lottie
from PIL import Image

import requests

st.set_page_config(page_title="PowerApp Alternative", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Streamlit")

# This function is to load a lottie from a file 
def load_lottiefile(filepath:str):
    with open(filepath, "r") as f:
        return json.load(f)

# This function is to load a lottie from a url 
def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

lottie_url = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_1h70d9xc.json")
lottie_file = load_lottiefile("lottie_files/apps.json")
image1 = Image.open("images/image1.png")

with st.container():
    st.write("---") # this is divide line
    left_col, right_col = st.columns(2)
    with left_col: 
        st.subheader("left col")
        st.write("##")
        st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    with right_col:
        st_lottie(
            lottie_file,
            speed=1,
            reverse=True,
            loop=True,
            quality="high",
            width=200,
            height=200,
            key=None
            )

with st.container():
    st.write("---")
    st.write("##")
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(image1)
    with text_col:
        st.write("""
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
         text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has 
         survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was 
         popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop 
         publishing software like Aldus PageMaker including versions of Lorem Ipsum.
         """)

with st.container():
    st.write("---")
    st.subheader("Form")

contact_form = """
<form action="https://formsubmit.co/Tharushika.jkh@keells.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your email-address" required>
     <textarea name="message" placeholder="Details of ticket"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# calling the css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")




