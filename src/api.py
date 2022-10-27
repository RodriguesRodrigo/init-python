from fastapi import APIRouter


api = APIRouter()


@api.get("/healthcheck/", name="healthcheck")
def healthcheck() -> dict[str]:
    return {"status": "ok"}


# Here you can add the routers of your modules
# api.include_router(...)
