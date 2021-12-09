from __future__ import annotations
import asyncio
from collections import deque
import typing as t
from discord_interaction.abc import Context

class Emitter:
    def __init__(self) -> None:
        self.listeners= deque()
        self._loop = asyncio.get_event_loop()

    def add_listner(self, name: str | t.Any, callback: t.FunctionType):
        self.listeners.append({
            "name": name,
            "callback": callback
        })

    def remove_listner(self, name: str | t.Any):
        self.listeners.remove([listner for listner in self.listeners if listner["name"] == name])
    
    def emit(self, name: str | t.Any, context: Context):
        listner = [i for i in self.listeners if i["name"] == name]
        if not listner:
            return
        callback = listner[0]["callback"]
        if asyncio.iscoroutinefunction(callback):
            self._loop.run_until_complete(callback())
