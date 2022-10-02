import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "19077894"))
API_HASH = getenv("API_HASH", "43aa5806e117b8422c9ee9b22589812c")
BOT_TOKEN = getenv("BOT_TOKEN", "5728652648:AAGIfIYdh35ZIC6bS1yxX_cyC140AqnKgDM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQAYewHixZUoOMi0nJoVSP_KsCzn5SIlEBpavjwyuWFExzBsB3PLvasO1mnikpjVmv3TaSiaT7xy7FFv6XVtYDru9gSJQ5nXbXKbRMImgdaGBlrahIB-K86YczPdN9Tao54ODQH3p69fjL4uQ9JinwQfSNVh7Pax65hIKkcWHUItUVLL5LBt-JzLYdE4x2-b2B0Mz1OccUFNJp124YeVvESYIiQRVURw14LFdEI2y3-SsS6Fal6Ur0tsiPdMjn615IAXnCIbvJoR3bFx8qJqyPJHN5Y1-iadTehtAug5QNbeTdgaRP0e7W4uWWFU3zfziiRww4inS8xxZgox2Qr6Gc2CAAAAAUdkje0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
