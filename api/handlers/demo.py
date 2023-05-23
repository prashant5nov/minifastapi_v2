from fastapi import APIRouter
from api.responses.detail import DetailResponse


router = APIRouter()


@router.get("/hello-world", response_model=DetailResponse)
def hello_world():
    return DetailResponse(message="Hello World!!!")
