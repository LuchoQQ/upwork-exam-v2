from fastapi import APIRouter, HTTPException
import uuid
from ..models.profile import Profile
from ..models.user import User
from ..data import users
from ..data import profiles

## initialize fastapi router
router = APIRouter(prefix="/users")

## create user
@router.post("/")
async def create_user(user: User):
    user.id = str(uuid.uuid4())  
    users.append(user)
    return {"message": "User created successfully", "user_id": user.id}


## get all users
@router.get("/")
async def get_users():
    return users

@router.get("/{user_id}")
async def get_user_by_id(user_id: str):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

## update user by id
@router.put("/{user_id}")
async def update_user_by_id(user_id: str, updated_user: User):
    global users  

    for index, user in enumerate(users):
        if user.id == user_id:
            updated_user_data = updated_user.model_dump(exclude_unset=True)
            for field, value in updated_user_data.items():
                setattr(users[index], field, value)
            
            return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")


## delete user by id
@router.delete("/{user_id}")
async def delete_user_by_id(user_id: str):
    global users, profiles

    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users = [u for u in users if u.id != user_id]
    
    profiles = [p for p in profiles if p.user_id != user_id]

    return {"message": "User and their profiles deleted successfully"}


## add profile to user
@router.put("/{user_id}/add_profile")
async def add_profile_to_user_by_id(user_id: str, profile: Profile):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    profile.id = str(uuid.uuid4())  
    profile.user_id = user_id
    
    user.profiles.append(profile)
    profiles.append(profile)

    return {"message": "Profile added successfully", "user": user.model_dump()}

@router.get("/{user_id}/favorite_profiles")
async def get_favorite_profiles(user_id: str):
    # Fetch the user from the database
    user = await get_user_by_id(user_id)  # Use 'await' here to get the actual user object
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Filter and retrieve the user's favorite profiles
    favorite_profiles = [profile.model_dump() for profile in user.profiles if profile.is_favorite]

    return {"favorite_profiles": favorite_profiles}