import redis
import os
from dotenv import load_dotenv
load_dotenv()

def r_con():
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        decode_responses=True,
    )
    return r

# CACHE_TTL = int(os.getenv("CACHE_TTL", "60"))






