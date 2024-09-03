from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_SERVER: str
    DB_NAME: str
    DB_DRIVER: str
    INITIAL_CATALOG: str
    TRUSTED_CONNECTION: str

    @property
    def DATABASE_URL_pyodbc(self):
        # Constructing the connection string with Initial Catalog and Trusted_Connection
        return (
            f"mssql+pyodbc://{self.DB_SERVER}/{self.INITIAL_CATALOG}?"
            f"driver={self.DB_DRIVER}&"
            f"Trusted_Connection={self.TRUSTED_CONNECTION}"
        )

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()



















# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     DB_SERVER: str
#     DB_NAME: str
#     DB_DRIVER: str

#     @property
#     def DATABASE_URL_pyodbc(self):
#         # mssql+pyodbc://CZ-DBS1.dlubal.local/netgenium?driver=SQL+Server
#         return f"mssql+pyodbc://{self.DB_SERVER}/{self.DB_NAME}?driver={self.DB_DRIVER}"

    
#     model_config = SettingsConfigDict(env_file=".env")

# settings = Settings()
