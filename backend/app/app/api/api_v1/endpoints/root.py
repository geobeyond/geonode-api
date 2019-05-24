from typing import List
from fastapi import APIRouter, Body
from app.models.root import Link, link, root
from app.core.config import (
    WPS_SELF_LINK,
    WPS_SERVICE_LINK,
    WPS_LOCATION,
    get_wps_link,
    ApplicationType,
    WPSRel,
    Lang,
    Title
)


router = APIRouter()


@router.get("/", response_model=Link, status_code=200)
#def read_wps_landing_page(
#        links: List[link] = Body(
#            ...,
#            example={"links": [
#                {
#                    "href": "http://processing.example.org/",
#                    "rel": "self",
#                    "type": "application/json",
#                    "hreflang": "en-US",
#                    "title": "this document"
#                }
#            ]}
#        )
#    ):
def read_wps_landing_page():
    """
    Retrieve WPS API landing page.
    """

    from app.main import app

    routes = app.routes
    wps_links = [link(**WPS_SELF_LINK), link(**WPS_SERVICE_LINK)]
    tags = [route.tags[0] for route in routes if WPS_LOCATION in route.path]
    links = []
    for tag in tags:
        if tag == WPSRel.CONFORMANCE.value:
            links.append(link(
                **get_wps_link(
                    f"{WPS_LOCATION}/{tag}",
                    WPSRel.CONFORMANCE,
                    ApplicationType.JSON,
                    Lang.EN,
                    Title.CONFORMANCE
                )
            ))
    wps_links += links
    return root(links=wps_links)
