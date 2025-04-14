# utils.py

def print_header(title: str):
    print("\n" + "=" * 50)
    print(f"{title}")
    print("=" * 50)


def format_job_list(jobs: list) -> list:
    """
    Returns a sorted list of job names from a list of job dictionaries.
    """
    return sorted(job.get("settings", {}).get("name", "Unnamed Job") for job in jobs)
