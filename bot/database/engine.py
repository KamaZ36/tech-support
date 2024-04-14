from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def create_database_pool(url: str, logging: bool = False) -> async_sessionmaker:
    engine = create_async_engine(url=url, echo=logging)
    return async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)