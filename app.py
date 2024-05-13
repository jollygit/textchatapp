# Import required modules
import os
from langchain_core.messages import ChatMessage
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from google.colab import userdata

GOOGLE_API_KEY_VALUE="AIzaSyCoOD9kfy6T-3GmykPbASEvNByaDqZjwfQ"

# Set up your Google API Key in os environment #if "GOOGLE_API_KEY"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY_VALUE

# Initialize the Gemini vision model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Example usage: Invoke the model to perform a task
#result = llm.invoke("What is the meaning of Jolly")

st.title('Simple Q&A with Gemini API')
st.write('## This app is running on `Streamlit` + `Google Colab` using `Langchain`, `Gemini API` with `Python` programming and `pyngrok` ')
st.markdown("This app will give response for any question using <span style='color: blue;'>__Gemini__</span>", unsafe_allow_html=True)
#st.write(result.content)
#st.write(result) if you are using GoogleGenerativeAI class
# Create a text input field
question = st.text_input("Enter your question in one line:")
submit = st.button("Generate response")

# Display the entered text as a title
if submit:
  if question:
    answer=llm.invoke(question)
    st.write("Response:" + answer.content)

