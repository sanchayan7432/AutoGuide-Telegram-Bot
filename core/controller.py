from core.prompt_builder import build_prompt
from llm.groq_client import generate_answer
from defense.sanitizer import sanitize
from defense.injection_guard import detect_injection
from core.formatter import enforce_word_limit
from config.settings import MARKS_RULES
from utils.logger import logger
from core.fallback_engine import fallback_answer


class AutoGuideController:

    def get_answer(self, question, marks):

        try:
            logger.info(f"Received question: {question}")
            logger.info(f"Marks: {marks}")

            # 🚫 Injection detection
            if detect_injection(question):
                logger.warning("Injection detected")
                return "Unsafe question detected."

            # 🧹 Sanitize
            question = sanitize(question)

            # 🧠 Prompt
            prompt = build_prompt(question, marks)

            # 🤖 AI Call
            raw_answer = generate_answer(prompt)

            # 🔥 FINAL SAFETY (IMPORTANT)
            if not raw_answer:
                logger.warning("AI failed, using fallback engine")
                raw_answer = fallback_answer(question, marks)

            # 📏 Word control
            min_w, max_w = MARKS_RULES.get(marks, (100, 120))
            final_answer = enforce_word_limit(raw_answer, min_w, max_w)

            return final_answer

        except Exception as e:
            logger.error(f"Controller Error: {str(e)}")
            return "Error generating answer."