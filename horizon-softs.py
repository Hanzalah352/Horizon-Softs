import streamlit as st
import os
import PIL
try:
    if os.path.exists("image.jfif"):
        favicon_img = PIL.Image.open("image.jfif")
        st.set_page_config(
            page_title="Horizon Softwares",
            page_icon=favicon_img,
            layout="centered"
        )
    else:
        st.set_page_config(page_title="Horizon Softwares", layout="centered")
except Exception as e:
    st.set_page_config(page_title="Horizon Softwares", layout="centered")
st.title("**Welcome** ***to*** *Horizon Softwares*")
st.header("**About Us**")
Horizon = ['Horizon is doing its best to make you happy','You can visit us at horizon-softwares.netlify.app','We are always here to help you with your needs','Horizon is a software development company that specializes in creating innovative solutions for businesses and individuals.']
# writes all the elements of the list Horizon in the streamlit app using matrix
for i in range(len(Horizon)):
    st.write(f"{i+1}. {Horizon[i]}")
st.divider()
st.header('Build Softwares that you need.')
name = st.text_input("Your Name:","")
age = st.slider('Your Age', 0, 100, 25)
gender = st.radio("Select your gender:", ('Male', 'Female', 'Other' , 'Prefer not to say'))
country = st.selectbox('Select your country:', ('USA', 'Canada', 'UK', 'Australia', 'Other'))
software_idea = st.text_input("Your Software Idea:","")
st.toggle('I accept privacy policy')

def idea():
    st.success("Thank you for sharing your idea with us! We will get back to you soon.Contact us at horizon-softwares.netlify.app for any queries or Software Ideas.")
    st.write('**Your Idea and Request:**')
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Country: {country}")
    st.write(f"Software Idea: {software_idea}")

if age < 18:
    st.warning("You must be at least 18 years old to submit your idea.")
if st.button('Submit') :
    idea()
    st.caption('We have given you your request as a message so send it on horizon-softwares.netlify.app for any queries or Software Ideas using our email.')
    st.write('**Contact Us:**')
    st.code('horizonsofts8@gmail.com', language='Email')
