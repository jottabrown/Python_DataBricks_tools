from src.domain.entities.job_schedule import JobSchedule

class ListSchedulesUseCase:
    def __init__(self, databricks_api):
        self.api = databricks_api

    def execute(self):
        jobs = self.api.get_all_jobs()
        schedules = []

        for job in jobs:
            if "schedule" in job.get("settings", {}):
                schedules.append(JobSchedule(
                    job_id=job["job_id"],
                    name=job["settings"].get("name", "Unnamed"),
                    schedule=job["settings"]["schedule"]
                ))

        return schedules
