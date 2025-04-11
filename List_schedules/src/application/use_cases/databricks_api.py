import requests

class DatabricksAPI:
    def __init__(self, settings):
        self.base_url = f"{settings.instance}/api/2.1/jobs/list"
        self.token = settings.token
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_all_jobs(self):
        response = requests.get(self.base_url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("jobs", [])
