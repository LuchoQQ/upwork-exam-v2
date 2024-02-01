from fastapi import APIRouter, HTTPException
import uuid
from ..models.profile import Profile
from ..models.user import User
from ..data import users
from ..data import profiles
# initialize fastapi router
router = APIRouter(prefix="/users")



# Create user
@router.post("/")
async def create_user(user: User):
    user.id = str(uuid.uuid4())  
    users.append(user)
    return {"message": "User created successfully", "user_id": user.id}


# Get all users
@router.get("/")
async def get_users():
    return users

@router.get("/{user_id}")
async def get_user(user_id: str):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user by id
@router.put("/{user_id}")
async def update_user(user_id: str, updated_user: User):
    global users  # If 'users' is a global list

    # Find the user to update
    for index, user in enumerate(users):
        if user.id == user_id:
            # Update only the provided fields using model_dump
            updated_user_data = updated_user.model_dump(exclude_unset=True)
            for field, value in updated_user_data.items():
                setattr(users[index], field, value)
            
            return {"message": "User updated successfully"}

    # If user not found, raise an HTTPException
    raise HTTPException(status_code=404, detail="User not found")


# Delete user by id
@router.delete("/{user_id}")
async def delete_user(user_id: str):
    global users  # If 'users' is a global list
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    users = [u for u in users if u.id != user_id]
    return {"message": "User deleted successfully"}


# Add profile to user
@router.put("/{user_id}/add_profile")
async def add_profile_to_user(user_id: str, profile: Profile):
    # Your logic here
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    profile.id = str(uuid.uuid4())  
    # Add the profile to the user's profiles
    user.profiles.append(profile)
    profiles.append(profile)

    return {"message": "Profile added successfully", "user": user.dict()}
