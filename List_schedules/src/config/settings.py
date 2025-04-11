from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.instance = os.getenv("DATABRICKS_INSTANCE")
        self.token = os.getenv("DATABRICKS_TOKEN")

        if not self.instance or not self.token:
            raise ValueError("Missing environment variables for Databricks config.")