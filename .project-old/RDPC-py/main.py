from fastapi import FastAPI
from Routers import users_router, articles_router

app = FastAPI()

# Incluindo os routers
app.include_router(users_router)
app.include_router(articles_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
