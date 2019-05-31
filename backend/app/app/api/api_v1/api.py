from fastapi import APIRouter
from fastapi.routing import APIRoute

from app.api.api_v1.endpoints import (
    items,
    login,
    users,
    utils,
    conformance,
    root,
    processes
)
from app.core.config import WPS_LOCATION, WPSRel

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(
    root.router,
    prefix=f"/{WPS_LOCATION}",
    tags=["root"]
)
api_router.include_router(
    conformance.router,
    prefix=f"/{WPS_LOCATION}",
    tags=[WPSRel.CONFORMANCE.value]
)
api_router.include_router(
    processes.router,
    prefix=f"/{WPS_LOCATION}",
    tags=[WPSRel.PROCESSES.value]
)
