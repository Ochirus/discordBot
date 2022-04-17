import random
import requests

from typing import Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag

# --Tam-U
# --Kyockcho
# --Endou Okito
# --ratatatat74

class HentaiLib:
    def __init__(self, author: Union[str, None], title: Union[str, None]):
        self.author = author
        self.title = title

    @property
    def GetRandomLink(self) -> str:
        with open("Links/HentaiLibLinks.txt", "r") as LinkFile:
            text = LinkFile.readlines()
            line = random.randint(0, len(text) - 1)

            url = text[line]
            print(text)
            response = requests.get(url)
            html = response.text

            tag_contents = [tag.get('href') for tag in get_tags(html, 'a', 'media-card')]
            href = random.randint(0, len(tag_contents) - 1)
            return tag_contents[href]

    @staticmethod
    def GetRandomAuthorLink() -> str:
        pass

    @staticmethod
    def GetLink() -> str:
        pass


def get_tags(html: str, name: str, class_: Union[str, bool, None]) -> ResultSet[Tag]:
    html = BeautifulSoup(html, 'html.parser')
    return html.find_all(name=name, class_=class_)
