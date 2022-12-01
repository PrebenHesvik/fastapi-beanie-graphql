import beanie
import motor
import motor.motor_asyncio


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(
        database=client.db_name, document_models=[TodoList, TodoItem]  # type: ignore
    )
