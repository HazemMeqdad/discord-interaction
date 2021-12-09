from __future__ import annotations
from enum import Enum
import typing

@typing.final
class InteractionType(Enum):
    PING = 1
    """
    To verify interaction request
    """
    APPLICATION_COMMAND = 2
    """
    SlashCommands & UserCommand & MessageCommand
    """
    MESSAGE_COMPONENT = 3
    """
    Component respone
    """
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    """
    I do't know
    """


class OptionType:
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    """
    Any integer between -2^53 and 2^53
    """
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    """
    Includes all channel types + categories
    """
    ROLE = 8
    MENTIONABLE = 9
    """
    Includes users and roles
    """
    NUMBER = 10
    """
    Any double between -2^53 and 2^53
    """
