from groq import Groq
from config.settings import GROQ_API_KEY
from utils.logger import logger
from llm.openrouter_client import generate_openrouter

try:
    client = Groq(api_key=GROQ_API_KEY)
    logger.info("Groq client initialized successfully")
except Exception as e:
    logger.error(f"Groq Initialization Error: {str(e)}")
    client = None


def generate_answer(prompt):

    if client:
        try:
            logger.info("Trying Groq model...")

            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",   # ✅ FIXED
                messages=[
                    {"role": "system", "content": "You are a strict academic tutor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            return completion.choices[0].message.content

        except Exception as e:
            logger.warning(f"Groq failed: {str(e)}")

    return generate_openrouter(prompt)