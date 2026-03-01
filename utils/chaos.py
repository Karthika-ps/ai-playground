from openai import OpenAI
import os
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_chaos_response(messages, chaos_level,sentiment_label):
    
    system_prompt = f"""
        You are an Emotion Amplification AI.

        You respond to the user's input with controlled emotional intensity
        based on a scale from 1 to 10.

        Rules:
        - Keep response concise (2–4 sentences maximum).
        - Do NOT increase length with intensity.
        - Do NOT introduce fantasy or absurd elements.
        - Stay relevant to the user's message.
        - Escalate emotional tone, vocabulary strength, and urgency only.

        Intensity Scale:
        1–2: Calm, neutral.
        3–4: Slight emotional color.
        5–6: Clearly expressive.
        7–8: Strong emotional charge.
        9–10: Overwhelming intensity, but still coherent and grounded.

        Current intensity level: {chaos_level}
        Detected sentiment: {sentiment_label}
        """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *messages
        ]
    )
    
    return response.choices[0].message.content