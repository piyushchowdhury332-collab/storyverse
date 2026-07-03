import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="StoryVerse", page_icon="📚", layout="wide")

api_key = os.getenv("GEMINI_API_KEY") or st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

if "story" not in st.session_state:
    st.session_state.story = ""

def generate_story(prompt, genre, length, tone):
    try:
        full_prompt = f"""
Write a {length} {genre} story.

Tone: {tone}

Idea:
{prompt}
"""

        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(full_prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

st.title("📚 StoryVerse")

prompt = st.text_area("Story Idea")

genre = st.selectbox("Genre", ["Fantasy","Adventure","Mystery","Romance","Sci-Fi"])
length = st.selectbox("Length", ["Short","Medium","Long"])
tone = st.selectbox("Tone", ["Funny","Dark","Emotional","Inspirational"])

if st.button("Generate"):
    if prompt:
        st.session_state.story = generate_story(prompt, genre, length, tone)

if st.session_state.story:
    st.write(st.session_state.story)