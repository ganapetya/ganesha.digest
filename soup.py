from bs4 import BeautifulSoup

def clean(html: str) -> str:
    # Parse HTML content
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove all JavaScript and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Extract text
    text = soup.get_text(separator=" ", strip=True)
    return text

