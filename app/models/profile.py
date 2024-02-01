from pydantic import BaseModel
from typing import List, Optional

class Profile(BaseModel):
    id: Optional[str] = None
    name: str
    description: str