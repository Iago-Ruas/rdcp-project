from fastapi import APIRouter, HTTPException, status
from Services import user_service
from schemas import UserCreator

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users():
    return {"message": "Lista de usuários"}


@router.post("/")
async def post_user(User: UserCreator):
    service = await user_service.create_user(User)

    if service == "503 - Service Err":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="user_service err ln24",
        )

    return status.HTTP_201_CREATED
