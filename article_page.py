from typing import List
from dataclasses import dataclass

@dataclass
class ArticlePage:
    title: str
    paragraphs: List[str]

    def to_content(self) -> str:
        content = f"Title:\n{self.title}\nParagraphs:\n"
        content += "\n".join(self.paragraphs)
        return content

    def is_article(self) -> bool:
        return True
