from telegram import Update
from telegram.ext import ContextTypes
from core.controller import AutoGuideController
from utils.logger import logger

controller = AutoGuideController()
user_state = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"User {update.message.chat_id} started bot")

    await update.message.reply_text(
        "AutoGuide AI Tutor\n\nSend your question."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    text = update.message.text.strip()

    logger.info(f"User {user_id} message: {text}")

    try:
        # Step 1: Question Input
        if user_id not in user_state:
            user_state[user_id] = {"question": text}

            logger.debug(f"Stored question for user {user_id}")

            await update.message.reply_text(
                "Enter marks (2 / 5 / 10):"
            )

        # Step 2: Marks Input
        else:
            question = user_state[user_id]["question"]
            marks = text

            if marks not in ["2", "5", "10"]:
                logger.warning(f"Invalid marks from user {user_id}: {marks}")

                await update.message.reply_text(
                    "Invalid input. Enter marks: 2 / 5 / 10"
                )
                return

            await update.message.reply_text("Generating answer...")

            logger.info(f"Processing question for user {user_id}")

            answer = controller.get_answer(question, marks)

            await update.message.reply_text(answer)
            await update.message.reply_text("Ask next question.")

            logger.info(f"Response sent to user {user_id}")

            # Reset state
            user_state.pop(user_id)

    except Exception as e:
        logger.error(f"Handler Error for user {user_id}: {str(e)}")

        await update.message.reply_text(
            "Something went wrong. Please try again."
        )