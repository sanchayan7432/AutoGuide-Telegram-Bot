import requests
import os
from utils.logger import logger

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_openrouter(prompt):

    try:
        logger.info("Using OpenRouter fallback...")

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openchat/openchat-7b",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        # DEBUG (important)
        logger.debug(f"OpenRouter raw response: {data}")

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        if "error" in data:
            logger.error(f"OpenRouter API Error: {data['error']}")
            return None

        return None

    except Exception as e:
        logger.error(f"OpenRouter Exception: {str(e)}")
        return None