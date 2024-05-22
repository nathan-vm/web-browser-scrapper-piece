from pydantic import BaseModel, Field
from typing import List

class CommandInput(BaseModel):
    name: str
    cmd: str
    stop_on_error: bool

class CommandOutput(BaseModel):
    name: str
    result: str


class InputModel(BaseModel):
    """
    Selenium Web Browser Input Model
    """

    commands: List[CommandInput] = Field(
        default=1,
        description="Number of seconds to sleep",
    )


class OutputModel(BaseModel):
    """
    Selenium Web Browser Output Model
    """
    outputs: List[CommandOutput] = Field(
        description="Outputs in order of each command input. Missing results are declared as 'None'."
    )
