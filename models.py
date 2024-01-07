from pydantic import BaseModel, Field
from typing import Optional

class DataPY(BaseModel):
    """
        Pydantic model to match and validate the incoming parameters
        
        """
    id: Optional[int]
    media_url: str
    caption: str