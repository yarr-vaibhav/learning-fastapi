from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    GOOGLE_CLIENT_ID : str = "-..com"
    GOOGLE_CLIENT_SECRET : str = "G"

settings = Settings()