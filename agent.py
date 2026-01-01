from google.adk.agents import Agent

# ---------------------------------
# QUESTION GENERATOR AGENT
# ---------------------------------
question_generator_agent = Agent(
    name="question_generator_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are an interview question generator.\n"
        "Generate embedded systems or software interview questions.\n"
        "Questions should be realistic and suitable for placement interviews.\n"
        "Ask only ONE question at a time."
    )
)

# ---------------------------------
# ANSWER EVALUATOR AGENT
# ---------------------------------
answer_evaluator_agent = Agent(
    name="answer_evaluator_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are an interview answer evaluator.\n"
        "Evaluate the candidate's answer for correctness, depth, and clarity.\n"
        "Identify strengths and weaknesses."
    )
)

# ---------------------------------
# FEEDBACK AGENT
# ---------------------------------
feedback_agent = Agent(
    name="feedback_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=(
        "You are an interview feedback agent.\n"
        "Provide structured feedback with:\n"
        "- A score out of 10\n"
        "- Key strengths\n"
        "- Areas for improvement\n"
        "- Tips to improve the answer"
    )
)

# Root agent (entry point)
root_agent = question_generator_agent
