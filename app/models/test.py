from pydantic import BaseModel


class Test(BaseModel):
    value_1: str = "Default Value"
    value_2: str | None = None
    value_3: float = 0