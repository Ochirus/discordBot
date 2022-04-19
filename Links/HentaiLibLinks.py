import random
import requests
import urllib3

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
        self.tag_contents = None

    def SetAuthor(self, author: str):
        self.author = author

    def SetTitle(self, title: str):
        self.title = title

    def GetTag_contents_size(self):
        return len(self.tag_contents)

    def GetRandomLink(self) -> str:
        with open("Links/HentaiLibLinks.txt", "r") as LinkFile:
            text = LinkFile.readlines()
            line = random.randint(0, len(text) - 1)

            url = text[line][0: len(text[line]) - 1]
            print(url)
            http = urllib3.PoolManager()
            response = http.request('GET', url, preload_content=False)
            print(response)

            tag_contents = [tag.get('href') for tag in get_tags(response, 'a', 'searchcontent')]
            print(len(tag_contents))
            href = random.randint(0, len(tag_contents) - 1)
            # print(f'https://m-hentai.net/{tag_contents[href]}')
            # print(type(f'https://m-hentai.net/{tag_contents[href]}'))

            href = f'https://m-hentai.net/{tag_contents[href]}'
            response = http.request('GET', href, preload_content=False)
            self.tag_contents = [tag.get('data-src') for tag in get_tags(response, 'img', 'lazyloadimage')]

    def GetLinkImage(self, iterator: int) -> str:
        return self.tag_contents[iterator]

    @staticmethod
    def GetRandomAuthorLink() -> str:
        pass

    @staticmethod
    def GetLink() -> str:
        pass


def get_tags(html: str, name: str, class_: Union[str, bool, None]) -> ResultSet[Tag]:
    html = BeautifulSoup(html, 'lxml')
    # print(html)
    return html.find_all(name=name, class_=class_)
