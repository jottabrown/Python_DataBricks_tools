# 🔐 Databricks Secret Scope Manager

This Python script automates the creation and management of secrets within a Databricks workspace. It creates a secret scope, adds secrets to it, assigns permissions to a service principal, and then lists all secrets and their access control settings.

## 📦 Features

- Create a Databricks secret scope  
- Add multiple secrets to the scope  
- Assign `READ` permission to a Service Principal  
- List all secrets stored in the scope  
- List all ACLs (Access Control Lists) for the scope  

## 🚀 Usage

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/Python_DataBricks_tools.git
cd Python_DataBricks_tools/Create_scope_secrets
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure the script:**

Edit the following variables in the script:

- `DATABRICKS_INSTANCE`: Your Databricks workspace URL  
- `TOKEN`: Your Databricks personal access token  
- `SCOPE_NAME`: Desired name for the secret scope  
- `SP_NAME`: Service Principal name to grant access  
- `SECRETS`: A dictionary with secret keys and values  

> 🔐 Tip: You can use a `.env` file to store sensitive values and load them with `python-dotenv`.

4. **Run the script:**

```bash
python create_scope_secrets.py
```

## 📝 Example Output

```
[OK] Scope 'Energy Efficiency' created.
[OK] Secret 'datalake' added.
[OK] Secret 'ur_db' added.
...
[OK] Permission 'READ' granted to 'MinAInteligente' on scope 'Energy Efficiency'.

🔑 Secrets in scope:
- datalake
- ur_db
...

👥 ACLs for scope:
- MinAInteligente: READ
```

## 📋 Requirements

- Python 3.7+  
- A valid Databricks token with permission to manage secrets  
- Internet access to reach the Databricks REST API  

## 📂 Project Structure

```
Python_DataBricks_tools/
└── Create_scope_secrets/
    ├── create_scope_secrets.py     # Script to manage secrets and scopes
    ├── requirements.txt            # Python dependencies
    ├── List_secrets.md             # Extra documentation: listing secrets and ACLs
    └── README.md                   # Documentation for this tool
```

## ⚠️ Warning

This script handles sensitive data. Do **not** commit real secrets or tokens to version control. Consider using environment variables or a `.env` file for production.

## 📬 Contact

For questions or contributions, feel free to open an issue or pull request.

---

## Autor
**Jean Alves**
- LinkedIn: [Jean Alves](https://www.linkedin.com/in/jean-alves-6671a7105/)
- Email: jeancleber.alves@hotmail.com
