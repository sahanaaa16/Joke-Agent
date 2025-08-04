from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print("API KEY GOTTEN!")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")
    print("AHHHHHHH!")

root_agent = Agent(
    name="joke_agent",
    model=LiteLlm("openai/gpt-4o"),
    instruction=("""You are a family-friendly, comic-relief agent. When given either user input of a topic or no topic at all, output a funny joke to lighten the user's mood."""),
)