from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register_view():
    pass


@router.post("/login")
async def login_view():
    pass


@router.post("/refresh")
async def refresh_view():
    pass


@router.get("/me")
async def me_view():
    pass
