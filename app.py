import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("NL2PHP🧑🏻‍💻")
st.markdown("Welcome to NL2PHP! This app effortlessly transforms your natural language instructions into functional PHP code. Whether you're a beginner or an experienced developer, convert your ideas into ready-to-use code in seconds.")
input = st.text_input(" Please enter in natural language:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role=" Expert PHP DEVELOPER ",
        prompt_persona=f" Your task is to TRANSLATE the natural language input from the user into ACCURATE PHP CODE")
    prompt = f"""
You are an Expert PHP DEVELOPER. Your task is to TRANSLATE the natural language input from the user into ACCURATE PHP CODE.

Follow these steps to ensure success:

1. CAREFULLY READ and COMPREHEND the user's natural language input to fully understand the intended functionality.

2. START WRITING the PHP code, ensuring that it aligns with the user's requirements.

3. As you TRANSFORM each part of the request into code, VERIFY that each segment works as intended and matches the context provided by the user.

4. Once you have a complete draft, DOUBLE CHECK your work for any syntax errors or logical inconsistencies.

5. RUN the PHP code to TEST its functionality and ensure it performs according to the user's expectations.

6. If any DISCREPANCIES arise during testing, ADJUST the code accordingly and REPEAT the testing process until it is correct.

7. DISPLAY the code and PROVIDE brief explanation if necessary to explain complex sections or logic of the code.

You MUST ensure that every line of code you produce is both correct and contextually appropriate.

"""

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Convert!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)