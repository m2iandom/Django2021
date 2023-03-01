from pydantic import BaseSettings


class Settings(BaseSettings):
    database_name: str
    database_host: str
    database_username: str
    database_password: str
    secret_key: str
    Algorithm: str
    access_token_expire_min: int
    email_host: str
    email_port: int
    email_use_tls: bool
    email_user: str
    email_password: str

    class Config:
        env_file = ".env"


settings = Settings()
