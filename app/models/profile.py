from pydantic import BaseModel
from typing import List, Optional

class Profile(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[str] = None
    is_favorite: bool = False 
