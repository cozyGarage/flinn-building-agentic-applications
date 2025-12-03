from langchain_core.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

_tool_prompt = """\
Extract and parse recipe content from a given URL.

Use this tool when the user provides a link to a recipe and asks for details or wants to save it.

It returns the cleaned text content of the webpage, filtered to remove navigation, ads, and boilerplate, allowing you to parse ingredients and instructions effectively.
"""


@tool(description=_tool_prompt)
def recipe_management_extract_recipe_from_url(url: str) -> str:
    loader = WebBaseLoader(url)
    # Using lazy_load to be efficient, though we just need the first/only page for a single URL
    pages = list(loader.lazy_load())

    if not pages:
        return "No content found at the provided URL."

    # Combine content from all pages
    full_content = ""
    for doc in pages:
        # Parse HTML with BeautifulSoup to clean it
        soup = BeautifulSoup(doc.page_content, "html.parser")

        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()

        # Get text
        text = soup.get_text()

        # Break into lines and remove leading/trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = "\n".join(chunk for chunk in chunks if chunk)

        full_content += text + "\n\n"

    return full_content.strip()
