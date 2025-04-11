from src.infrastructure.databricks.databricks_api import DatabricksAPI
from src.application.use_cases.list_schedules import ListSchedulesUseCase
from src.config.settings import Settings

if __name__ == "__main__":
    settings = Settings()
    api = DatabricksAPI(settings)
    use_case = ListSchedulesUseCase(api)

    print("\n🗓️  List of Scheduled Jobs:\n" + "-" * 40)
    for schedule in use_case.execute():
        print(f"📌 Job ID: {schedule.job_id}")
        print(f"📛 Name: {schedule.name}")
        print(f"⏰ Schedule: {schedule.schedule}\n")
