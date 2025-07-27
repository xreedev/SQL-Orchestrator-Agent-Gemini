import json
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

class GeminiAgent :
    def __init__(self, agent_prompt):
        self.agent_prompt = agent_prompt

    def generate_evaluation(self, prompt: str) -> dict:
        full_prompt = self.agent_prompt + prompt
        text = model.generate_content(full_prompt).text

        # Remove triple backticks and optional language tags like ```json
        cleaned_text = re.sub(r"```(?:json)?\n?(.*?)```", r"\1", text, flags=re.DOTALL).strip()

        # Also remove any leftover single backticks if present
        cleaned_text = cleaned_text.replace("`", "").strip()

        # Now parse JSON safely
        return json.loads(cleaned_text)


