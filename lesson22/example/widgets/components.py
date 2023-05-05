from abc import ABC


class Component(ABC):
    def __init__(self, page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator


class Button(Component):
    def __init__(self):
        super().__init__()