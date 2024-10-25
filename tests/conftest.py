from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import pytest
from src.models import Base
from src.main import app


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "parking: маркер для тестов «Заезд на парковку» и «Выезд с парковки»"
    )


async_engine = create_async_engine(
    url='sqlite+aiosqlite:///./test.db',
    echo=True,
)


@pytest.fixture(scope='session')
async def async_db_engine():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield async_engine

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='function')
async def async_db(async_db_engine):
    async_session = sessionmaker(
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
        # bind=async_db_engine,
        # class_=AsyncSession,
    )


@pytest.fixture
async def client():
    # Создание тестового клиента
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
