from pydantic import BaseModel, Field
from typing import List

class InputModel(BaseModel):
    """
    Selenium Web Browser Input Model
    """

    get_page_html: List[str] = Field(
        default=["http://www.google.com.br"],
        description="URL you want to extract HTML",
    )

class OutputModel(BaseModel):
    """
    Selenium Web Browser Output Model
    """
    output_file_path: str = Field(
        description="Path for pickle file with a list of all HTML files combined."
    )
