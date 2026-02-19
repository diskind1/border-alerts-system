from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from routes import router
from mongo_connection import mongo_conn
from redis_connection import r_con

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_conn()        
    yield 
    r_con()

app = FastAPI(title="API's analytics" ,lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)