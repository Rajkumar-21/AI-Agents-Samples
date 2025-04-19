from typing import List
from agno.agent import Agent, RunResponse  # noqa
from agno.models.groq import Groq
from pydantic import BaseModel, Field
from rich.pretty import pprint  # noqa
from dotenv import load_dotenv
load_dotenv()
import os

os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

class MovieScript(BaseModel):
    setting: str = Field(
        ..., description="Provide a nice setting for a blockbuster movie."
    )
    ending: str = Field(
        ...,
        description="Ending of the movie. If not available, provide a happy ending.",
    )
    genre: str = Field(
        ...,
        description="Genre of the movie. If not available, select action, thriller or romantic comedy.",
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )


json_mode_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You help people write movie scripts.",
    response_model=MovieScript,
)

json_mode_agent.print_response("Chennai")