import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DatabricksClient:
    def __init__(self, instance_env, token_env):
        self.base_url = os.getenv(instance_env).rstrip('/')
        self.token = os.getenv(token_env)

        if not self.base_url or not self.token:
            raise ValueError(f"Missing env vars for {instance_env} or {token_env}")

        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_jobs(self):
        url = f"{self.base_url}/api/2.1/jobs/list"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("jobs", [])
