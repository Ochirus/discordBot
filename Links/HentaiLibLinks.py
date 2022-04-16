import random

from typing import Union
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


class HentaiLib:
    def __init__(self):
        pass

    @staticmethod
    def GetRandomLink() -> str:
        pass

    @staticmethod
    def GetRandomAuthorLink() -> str:
        pass

    @staticmethod
    def GetLink() -> str:
        pass


def get_tags(html: str, name: str, class_: Union[str, bool, None]) -> ResultSet[Tag]:
    html = BeautifulSoup(html, 'html.parser')
    return html.find_all(name=name, class_=class_)
