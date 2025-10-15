from questdb.ingress import Protocol, Sender

from app.config import QUEST_ADDR, QUEST_PASS, QUEST_PORT, QUEST_USER

def ingress_connection():
    with Sender(Protocol.Http, QUEST_ADDR, QUEST_PORT, username=QUEST_USER, password=QUEST_PASS) as sender:
        yield sender