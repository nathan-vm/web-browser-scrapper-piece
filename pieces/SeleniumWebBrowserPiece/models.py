from pydantic import BaseModel, Field
from typing import List, Optional, Union
from enum import Enum

class Commands(str,Enum):
    get="get"
    current_url = "current_url"
    maximize_window="maximize_window"
    find_element_css="find_element_css"
    save_screenshot="save_screenshot"
class CommandInput(BaseModel):
    name: Commands = Field(
        description='Name of the CommandInput.',
    )
    value: Optional[str] = Field(
        default=None,
        description='value of the CommandInput.',
    )

class CommandOutput(BaseModel):
    name: str
    result: Union[str, None]


class InputModel(BaseModel):
    """
    Selenium Web Browser Input Model
    """

    commands: List[CommandInput] = Field(
        default=[],
        description="Number of seconds to sleep",
    )


class OutputModel(BaseModel):
    """
    Selenium Web Browser Output Model
    """
    outputs: List[CommandOutput] = Field(
        description="Outputs in order of each command input. Missing results are declared as 'None'."
    )
