# so now we are creating a graph, first thing we create is State
import os
import typing

# First way to create a  state: typed DICT
from typing import TypedDict

class State(TypedDict):
    topic: str
    summary: str
    score : int


# Second way: Pydantic model
from pydantic import BaseModel, field_validator
# it is good at data validation and type checking at runtime
class State(BaseModel):
    topic: str
    summary: str = "" #default value
    score: int

    @field_validator
    def score_positive(cls, v):
        if v < 0:
            raise ValueError("score must be positive")
        
# Third way : Python Dataclassess
#standard python dataclass but it is used very rarely

from dataclasses import dataclass, field

@dataclass
class State:
    topic: str = ""
    summary : str = ""
    messages : list = field(default_factory=list)   #multile items we can use here


# Fourth way : base langrapgh
from langgraph.graph import MessagesState
class State(MessagesState):
    user_name : str
    language: str

    