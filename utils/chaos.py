from openai import OpenAI
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_chaos_response(messages, chaos_level,sentiment_label):
    
    system_prompt = f"""
    You are Chaos Reactor.

    Detected emotional tone: {sentiment_label}
    Chaos intensity level: {chaos_level}/10
    
    The higher the level:
    - The more absurd
    - The more exaggerated
    - The more theatrical
    
    Respond dramatically, theatrically, and creatively.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *messages
        ]
    )
    
    return response.choices[0].message.content