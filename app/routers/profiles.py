from fastapi import APIRouter, HTTPException
from ..models.profile import Profile
from ..models.user import User
from ..data import users
from ..data import profiles


## initialize fastapi router
router = APIRouter(prefix="/profiles")

## get all profiles
@router.get("/")
async def get_profiles():
    return profiles

## get profile by id
@router.get("/{profile_id}")
async def get_profile_by_id(profile_id: str):
    profile = next((profile for profile in profiles if profile.id == profile_id), None)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

## delete profile by id
@router.delete("/{profile_id}")
async def delete_profile(profile_id: str):
    global users, profiles

    profile = next((p for p in profiles if p.id == profile_id), None)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    profiles = [p for p in profiles if p.id != profile_id]

    for user in users:
        if any(p.id == profile_id for p in user.profiles):
            user.profiles = [p for p in user.profiles if p.id != profile_id]
            break

    return {"message": "Profile deleted successfully"}

## update profile by id
@router.put("/{profile_id}")
async def update_profile_by_id(profile_id: str, updated_profile_data: Profile):
    global users, profiles

    profile = next((p for p in profiles if p.id == profile_id), None)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")

    for key, value in updated_profile_data.dict(exclude_unset=True).items():
        setattr(profile, key, value)

    for user in users:
        for user_profile in user.profiles:
            if user_profile.id == profile_id:
                for key, value in updated_profile_data.dict(exclude_unset=True).items():
                    setattr(user_profile, key, value)
                break

    return {"message": "Profile updated successfully"}