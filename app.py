import streamlit as st
from google import genai
import os

st.set_page_config(page_title="StoryVerse", page_icon="📚", layout="wide")

api_key = os.getenv("GEMINI_API_KEY") or st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

if "story" not in st.session_state:
    st.session_state.story = ""

def generate_story(prompt, genre, length, tone):
    full_prompt = f"""
Write a {length} {genre} story.

Tone: {tone}

Idea:
{prompt}

Rules:
- Add title
- Engaging story
- Proper paragraphs
- Strong ending
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    return response.text


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