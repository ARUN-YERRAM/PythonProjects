import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from moviepy.editor import VideoFileClip
from google.cloud import speech
import io

load_dotenv() 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are Youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def extract_youtube_transcript(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        raise e

def extract_local_transcript(local_video_path):
    try:
        video = VideoFileClip(local_video_path)
        audio_path = "audio.wav"
        video.audio.write_audiofile(audio_path)

        client = speech.SpeechClient()
        with io.open(audio_path, "rb") as audio_file:
            content = audio_file.read()
        
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="hi-IN"
        )

        response = client.recognize(config=config, audio=audio)
        transcript = " ".join([result.alternatives[0].transcript for result in response.results])
        return transcript
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("YouTube/Local Video Transcript to Detailed Notes Converter")
video_source = st.radio("Select Video Source:", ("YouTube URL", "Local File"))

youtube_link = ""
local_video_path = ""

if video_source == "YouTube URL":
    youtube_link = st.text_input("Enter YouTube Video Link:")
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if video_source == "Local File":
    local_video_file = st.file_uploader("Upload Local Video File", type=["mp4", "mkv", "avi", "mov"])

if st.button("Get Detailed Notes"):
    transcript_text = ""
    if video_source == "YouTube URL" and youtube_link:
        transcript_text = extract_youtube_transcript(youtube_link)
    elif video_source == "Local File" and local_video_file:
        with open("uploaded_video.mp4", "wb") as f:
            f.write(local_video_file.getbuffer())
        transcript_text = extract_local_transcript("uploaded_video.mp4")

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
