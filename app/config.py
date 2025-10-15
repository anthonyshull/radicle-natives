import os

from dotenv import load_dotenv

load_dotenv()

QUEST_ADDR = os.getenv("QUEST_ADDR", "localhost")
QUEST_PORT = int(os.getenv("QUEST_PORT", 9000))
QUEST_USER = os.getenv("QUEST_USER", "admin")
QUEST_PASS = os.getenv("QUEST_PASS", "quest")