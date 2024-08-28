from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_SERVER: str
    DB_NAME: str
    DB_DRIVER: str

    @property
    def DATABASE_URL_pyodbc(self):
        # mssql+pyodbc://CZ-DBS1.dlubal.local/netgenium?driver=SQL+Server
        return f"mssql+pyodbc://{self.DB_SERVER}/{self.DB_NAME}?driver={self.DB_DRIVER}"

    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()