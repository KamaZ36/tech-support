import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    load_dotenv()

    sqlalchemy_logging: bool = True  # Логирование sqlalchemy, в продакшене можно ставить False
    use_webhook: bool = False  # Использовать вебхуки. Так же потребуется настроить в файле .env
    skip_updating: bool = True  # Пропускать обновления, советую не трогать.
    use_redis: bool = True  # Использовать Redis?

    bot_token: str = os.getenv('BOT_TOKEN')

    redis_host: str = os.getenv('REDIS_HOST')

    postgres_host: str = os.getenv('POSTGRES_HOST')
    postgres_database: str = os.getenv('POSTGRES_DATABASE')
    postgres_user: str = os.getenv('POSTGRES_USER')
    postgres_password: str = os.getenv('POSTGRES_PASSWORD')

    admin_tg_id: int = os.getenv('ADMIN_TG_ID')

    throttle_time_spin: int = 5
    throttle_time_other: int = 3

    contact_text: str = os.getenv('TEXT_CONTACTS')

    # webhook_path: str = os.getenv('WEBHOOK_PATH')
    # webhook_host: str = os.getenv('WEBHOOK_HOST')
    # webhook_url: str = f'{webhook_host}{webhook_path}'
    # webapp_host: str = os.getenv('WEBAPP_HOST')
    # webapp_port: int = os.getenv('WEBAPP_PORT')
    # webhook_secret: str = os.getenv('WEBAPP_SECRET')

    def create_dsn_postgresql(self):
        return (
            'postgresql+asyncpg://'
            f'{self.postgres_user}:{self.postgres_password}@'
            f'{self.postgres_host}/{self.postgres_database}'
        )


settings = Settings()
