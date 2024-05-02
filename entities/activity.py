from pydantic import BaseModel


class DataBaseConnectionEntity(BaseModel):
    type: str
    calories: float
    activity_time: float
