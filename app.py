#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset",page_icon="✨")
st.title( "Growth Mindset Challenge: Streamlit Web App")

st.header("🌱 Welcome to your path of Growth!")
st.write("Each step forward is a step toward greatness. Challenges will shape you, opportunities will uplift you, and persistence will define you. Trust the process, believe in yourself, and keep growing! This app will help you stay motivated, achieve your goals, and reflect on your progress.")

#quote section
st.header("Quote of the Day!")
st.write("'Do not judge me by my success, judge me by how many times I fell down and got back up again.' — Nelson Mandela")
 
st.header("What's your Today's Challenge?")
user_input = st.text_input("Describe the challenge you are facing:")


#condition
if user_input:
    st.success(f"you are facing:{user_input}.Keep pushing forward towards to your goals")
else:
    st.warning("Tell us about your challenge to kickstart your journey!")

#reflex
st.header("Reflect on your Learning")
reflection= st.text_area("Write your project outcomes here:")

if reflection:
    st.success(f"Thoughtful observation! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow!Share about your hardships") 


#achievements
st.header("Embrace your accomplishment!") 
achievement=st.text_input("Share a recent success or milestone you've reached:")


if achievement:
    st.success(f"Congrats! You attained:{achievement}")
else:
    st.info("Every thick and thin counts! Share your's now")


#footer
st.write("-  -  -")
st.write("Be patient with yourself. You are growing stronger every day. The weight of the world will become lighter... and you will begin to shine brighter. Don't give up.")
st.write("Created by Sani-e-Zehra") 
