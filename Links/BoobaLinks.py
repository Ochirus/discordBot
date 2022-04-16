import random

from typing import Union


class BoobaImage:
    def __init__(self, link: str, name: str, tags: [Union[str, None]]):
        self.link = link
        self.name = name
        self.tags = tags

    @staticmethod
    def GetBoobaLinksRandom() -> str:
        with open("Links/BoobaLinks.txt", "r") as LinkFile:
            text = LinkFile.readlines()
            line = random.randint(0, len(text) - 1)
            return text[line]

    @staticmethod
    def GetBoobaLinkLast() -> str:
        with open("Links/BoobaLinks.txt", "r") as LinkFile:
            text = LinkFile.readlines()
            line = len(text) - 1
            return text[line]
