from config.settings import MARKS_RULES

def build_prompt(question, marks):

    if marks == 2:
        instruction = (
            "Answer the question in 2-3 concise bullet points with starter sentence. "
            "Keep it very short and to the point within 40-60 words."
        )

    elif marks == 5:
        instruction = (
            "Answer the question in about 5-6 well-explained bullet points with starter sentence. "
            "Keep it clear, structured, and moderately detailed within 120-160 words."
        )

    elif marks == 10:
        instruction = (
            "Answer the question in a detailed manner with 8-12 points with starter sentence. "
            "Include explanations, examples (if possible), and deeper insights within 160-200 words."
        )

    else:
        instruction = "Answer clearly and concisely."

    prompt = f"""
You are an academic exam answer generator.

Question:
{question}

Instructions:
{instruction}

Format:
- Use numbered bullet points
- Do not add unnecessary text
- Keep answers exam-oriented
"""

    return prompt








# def build_prompt(question, marks):
#     min_w, max_w = MARKS_RULES.get(marks, (100, 120))

#     return f"""
# You are an expert B.Tech Computer Science tutor.

# STRICT INSTRUCTIONS:
# - Answer must be between {min_w} and {max_w} words
# - Format: Numbered points
# - No extra explanation
# - Exam-oriented answer only

# Question:
# {question}
# """