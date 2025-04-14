# 🆚 Compare Envs

This tool compares resources between two Azure Databricks workspaces using the Databricks REST API.

## 🎯 Purpose

Ensure consistency between environments (e.g., Dev vs Prod) by identifying missing or unmatched resources like jobs.

---

## ⚙️ Features

- 🔄 Compare jobs by name between two workspaces  
- 📌 Simple and clean architecture (Clean Code)  
- ⚡ Fast, no external dependencies besides `requests` and `dotenv`

---

## 🚀 Usage

1. Create a `.env` file in the root of `Compare_envs/`:

```env
# Workspace 1
DATABRICKS_INSTANCE_1=https://<workspace1>.cloud.databricks.com
DATABRICKS_TOKEN_1=your-token-1

# Workspace 2
DATABRICKS_INSTANCE_2=https://<workspace2>.cloud.databricks.com
DATABRICKS_TOKEN_2=your-token-2
```
2. Install dependencies:
  
```bash
pip install -r requirements.txt
```

3. run the comparison : 

```bash
python run.py

```

🧱 Project Structure

```bash

Compare_envs/
├── run.py                  # Entry point
├── databricks_client.py    # REST API client wrapper
├── comparer.py             # Comparison logic
├── utils.py                # Shared utilities (optional)
├── .env                    # Env config (not committed)
└── requirements.txt        # Python dependencies


```

## 📐 Design

This module uses clean code principles to keep logic simple and easy to extend.

## ⚠️ Warning

This script handles sensitive data. Do **not** commit real secrets or tokens to version control. Consider using environment variables or a `.env` file for production.

## 📬 Contact

For questions or contributions, feel free to open an issue or pull request.

---

## 🙋 Autor
**Jean Alves**
- LinkedIn: [Jean Alves](https://www.linkedin.com/in/jean-alves-6671a7105/)
- Email: jeancleber.alves@hotmail.com



