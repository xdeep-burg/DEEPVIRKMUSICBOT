""" mongo database """

from motor.motor_asyncio import AsyncIOMotorClient as Bot
from config import MONGODB_URL as aditya


MONGODB_CLI = Bot(aditya)
db = MONGODB_CLI.program
