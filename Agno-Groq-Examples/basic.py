from agno.agent import Agent, RunResponse  # noqa
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")
agent = Agent(model=Groq(id="qwen-2.5-32b"), markdown=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response on the terminal
agent.print_response("Share a 2 sentence horror story")