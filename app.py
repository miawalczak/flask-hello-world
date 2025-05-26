from openai import OpenAI
import autogen
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins by default


# Initialize the OpenAI client with your API key
os.environ["OPENAI_API_KEY"] = "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"

llm_config={
        "model": "gpt-3.5-turbo",
        "api_key": os.environ["OPENAI_API_KEY"]
    }

task = '''Write a concise but engaging blogpost about DeepLearning.AI. Make sure the blogpost is within 100 words.'''

writer = autogen.AssistantAgent(
    name="Writer",
    system_message="You are a writer. You write engaging and concise " 
        "blogpost (with title) on given topics. You must polish your "
        "writing based on the feedback you receive and give a refined "
        "version. Only return your final work without additional comments.",
    llm_config=llm_config,
)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    reply = writer.generate_reply(messages=[{"content": task, "role": "user"}])
    return jsonify(message=f"Blog, {reply}!")



