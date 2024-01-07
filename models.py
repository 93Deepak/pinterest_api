from pydantic import BaseModel, Field
from typing import Optional

class DataPY(BaseModel):
    id: Optional[int]
    media_url: str
    caption: str