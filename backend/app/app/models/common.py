from pydantic import BaseModel, Schema, UrlStr


class link(BaseModel):
    href: UrlStr = ...
    rel: str = None
    type: str = None
    hreflang: str = None
    title: str = None