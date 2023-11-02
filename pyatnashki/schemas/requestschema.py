from pydantic import BaseModel


class InputSchema(BaseModel):
    y: int
    x: int
