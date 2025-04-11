class JobSchedule:
    def __init__(self, job_id: int, name: str, schedule: dict):
        self.job_id = job_id
        self.name = name
        self.schedule = schedule

    def __repr__(self):
        return f"<JobSchedule id={self.job_id} name={self.name}>"
