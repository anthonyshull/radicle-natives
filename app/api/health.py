from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse
from questdb.ingress import IngressError, TimestampNanos

from app.db.quest import ingress_connection

router = APIRouter()

@router.get("/_health")
async def health_check(sender=Depends(ingress_connection)):
    try:
        sender.row("metrics", columns={"name": "health_check", "value": 1.0}, at=TimestampNanos.now())

        return PlainTextResponse("OK", status_code=200)
    except IngressError as e:
        return PlainTextResponse(str(e), status_code=500)