from __future__ import annotations
from discord_interaction.enums import OptionType

class Option:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    @property
    def name(self):
        return self.data.get("name")
    
    @property
    def type(self):
        return [i for i in OptionType.]
