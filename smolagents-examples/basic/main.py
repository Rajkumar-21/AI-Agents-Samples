import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool, Tool
import wikipediaapi
from datetime import datetime
import pytz

load_dotenv()

client = LiteLLMModel(api_base=os.getenv("API_BASE"), api_key=os.getenv("API_KEY"))
search_tool = DuckDuckGoSearchTool()
wiki_wiki = wikipediaapi.Wikipedia('en')
def get_current_time():
    """Get the current time in UTC."""
    tz = pytz.timezone('UTC')
    return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

def get_wikipedia_summary(query):
    """Get a summary of a Wikipedia page."""
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "No summary found."
def get_wikipedia_links(query):
    """Get links from a Wikipedia page."""
    page = wiki_wiki.page(query)
    if page.exists():
        return [link for link in page.links.keys()]
    else:
        return "No links found."
def get_wikipedia_categories(query):
    """Get categories from a Wikipedia page."""
    page = wiki_wiki.page(query)
    if page.exists():
        return [cat for cat in page.categories.keys()]
    else:
        return "No categories found."
