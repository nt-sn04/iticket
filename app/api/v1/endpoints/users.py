from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/users")
async def users_view():
    pass


@router.get("/users/{id}")
async def get_user_view(id: int):
    pass


@router.patch("/users/{id}")
async def update_user_view(id):
    pass
