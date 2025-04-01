from fastapi import APIRouter

router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/")
async def get_articles():
    return {"message": "Lista de artigos"}


@router.get("/{product_id}")
async def get_product(product_id: int):
    return {"message": f"Produto {product_id}"}
