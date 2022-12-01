from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter

authors: list[str] = []


@strawberry.type
class Query:
    @strawberry.field
    def all_authors(self) -> list[str]:
        return authors


@strawberry.type
class Mutation:
    @strawberry.field
    def add_author(self, name: str) -> str:
        authors.append(name)
        return name


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.on_event("startup")
async def connect():
    # await init_db()
    return {"message": "Todo app"}
