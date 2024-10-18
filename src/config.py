from pydantic_settings import BaseSettings

class Config(BaseSettings):
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    FPS: int = 60

    class Config:
        env_file = ".env"

config = Config()
