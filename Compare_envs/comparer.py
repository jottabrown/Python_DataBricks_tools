from databricks_client import DatabricksClient

def compare_jobs():
    ws1 = DatabricksClient("DATABRICKS_INSTANCE_1", "DATABRICKS_TOKEN_1")
    ws2 = DatabricksClient("DATABRICKS_INSTANCE_2", "DATABRICKS_TOKEN_2")

    jobs_1 = {job["settings"]["name"]: job for job in ws1.get_jobs()}
    jobs_2 = {job["settings"]["name"]: job for job in ws2.get_jobs()}

    all_job_names = set(jobs_1.keys()).union(jobs_2.keys())

    print("\n🔍 Comparing jobs between workspaces:\n")

    for name in sorted(all_job_names):
        in_1 = name in jobs_1
        in_2 = name in jobs_2

        if in_1 and in_2:
            print(f"✅ {name} - Exists in both")
        elif in_1:
            print(f"⬅️ {name} - Only in Workspace 1")
        else:
            print(f"➡️ {name} - Only in Workspace 2")
