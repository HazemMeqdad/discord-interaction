from __future__ import annotations
from discord_interaction.snowflask import Snowflake
from discord_interaction.enums import InteractionType

class Context:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    @property
    def id(self) -> Snowflake:
        return self.data.get("id")
    
    @property
    def command_id(self) -> Snowflake:
        return self.data["data"].get("id")
    
