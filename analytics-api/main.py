from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # init_run()          
    yield 

app = FastAPI(title="API's analytics" ,lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router)