# 📅 List Schedules

This tool lists all scheduled jobs in your Azure Databricks workspace using the Databricks REST API.

## 🚀 Usage

1. Configure your `.env` file:

```
DATABRICKS_INSTANCE=https://<your-instance>.cloud.databricks.com DATABRICKS_TOKEN=your-token-here

```

2. Install dependencies:

```bash
pip install -r requirements.txt

```
3. Run the script: 

```bash
python run.py

```

🧱 Architecture

This module follows modern software engineering principles to ensure high code quality, maintainability and testability:

- **Domain-Driven Design (DDD)**: separates business rules into domains.
- **S.O.L.I.D. principles**: ensures scalable and loosely coupled components.
- **Clean Architecture**: organizes the code in layers, isolating the core logic from infrastructure concerns.


```bash
src/
├── domain/         # Entities
├── application/    # Use cases
├── infrastructure/ # External services (Databricks API)
└── config/         # Environment settings
```