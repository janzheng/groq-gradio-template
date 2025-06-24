import gradio as gr
import groq_gradio
from groq import Groq
import os

from dotenv import load_dotenv
load_dotenv()  # pulls keys into os.environ

groq_api_key = os.environ.get("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

gr.load(
    name="llama-3.3-70b-versatile",  # The specific model powered by Groq to use; try llama-3.1-8b-instant
    src=groq_gradio.registry,  # Tells Gradio to use our custom interface registry as the source
    title="Groq x Gradio Template",  # The title shown at the top of our UI
    description="Chat with the Llama 3.3 70B model powered by Groq.",  # Subtitle
    examples=[
        "Explain quantum gravity to a 5-year old.",
        "How many R are there in the word Strawberry?",
    ],  # Pre-written prompts users can click to try
    # type="messages",  # Use the new messages format instead of deprecated tuples
).launch()  # Creates and starts the web server!
