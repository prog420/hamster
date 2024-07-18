import os

from dotenv import load_dotenv

load_dotenv()


class Env:
    BEARER_TOKEN = os.getenv('BEARER_TOKEN')
