from pydantic import BaseModel

"""These are the definitions for the data found in the TOML configuration
files."""


class Font(BaseModel):
    family: str
    size: int
    style: str
    leading: int
    weight: int


class Style(BaseModel):
    x_position: int
    y_position: int
    max_width: int
    max_height: int
    color: str
    font: Font
