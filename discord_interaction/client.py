from __future__ import annotations
from typing import Any
from flask import Flask
import gevent


class Client:
    def __init__(
        self, 
        application_id: int, 
        public_key: str | Any, 
        token: str | Any = None,
        endpoint_url: str = "/interactions"
    ) -> None:

        self.application_id = application_id
        self._public_key = public_key
        self.token: str | Any | None = token
        self.app = Flask(__name__)
        


    def run(self, port=5000, host="0.0.0.0"):
        self.app.run(host, port)
