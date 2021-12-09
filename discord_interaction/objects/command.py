from __future__ import annotations
from discord_interaction.snowflask import Snowflake

class Command:
    def __init__(self, data: dict) -> None:
        self.data = data

    @property
    def id(self) -> Snowflake:
        return self.data.get("id")
    
    @property
    def name(self) -> str:
        return self.data.get("name")
    
    @property
    def options(self) -> list:
        return
