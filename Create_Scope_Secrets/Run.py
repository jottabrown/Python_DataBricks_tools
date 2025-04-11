import requests
import json

# 🌐 Databricks instance and token (EXAMPLE ONLY)
DATABRICKS_INSTANCE = "https://<your-databricks-instance>"
TOKEN = "dapi<your-token>"

# 🔐 Secret scope and service principal
SCOPE_NAME = "example_scope"
SP_NAME = "example_service_principal"

# 🔑 Secrets to be added (example data only)
SECRETS = {
    "datalake": json.dumps({
        "account_name": "your_account",
        "client_id": "your_client_id",
        "tenant_id": "your_tenant_id",
        "client_secret": "your_client_secret",
        "timeout": "300s"
    }),
    "ur_db": json.dumps({
        "con": "mssql+pymssql://user:password@host/database"
    }),
    "cnx-example-01": "example_password_01",
    "cnx-example-02": "example_password_02",
    "cnx-example-03": "example_password_03"
}

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

# 📁 Create secret scope
def create_scope(scope_name: str) -> None:
    url = f"{DATABRICKS_INSTANCE}/api/2.0/secrets/scopes/create"
    response = requests.post(url, headers=HEADERS, json={"scope": scope_name})

    if response.status_code == 200:
        print(f"[✅] Scope '{scope_name}' created successfully.")
    elif "RESOURCE_ALREADY_EXISTS" in response.text:
        print(f"[ℹ️] Scope '{scope_name}' already exists.")
    else:
        print(f"[❌] Failed to create scope: {response.text}")

# 🔐 Add secrets to the scope
def add_secrets(scope_name: str, secrets: dict) -> None:
    url = f"{DATABRICKS_INSTANCE}/api/2.0/secrets/put"
    for key, value in secrets.items():
        payload = {
            "scope": scope_name,
            "key": key,
            "string_value": value
        }
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code == 200:
            print(f"[➕] Secret '{key}' added.")
        else:
            print(f"[❌] Failed to add secret '{key}': {response.text}")

# 👥 Grant read permission to a principal
def assign_acl(scope_name: str, principal: str, permission: str = "READ") -> None:
    url = f"{DATABRICKS_INSTANCE}/api/2.0/secrets/acls/put"
    payload = {
        "scope": scope_name,
        "principal": principal,
        "permission": permission
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"[👤] Permission '{permission}' granted to '{principal}'.")
    else:
        print(f"[❌] Failed to assign ACL: {response.text}")

# 📋 List all secrets in a scope
def list_secrets(scope_name: str) -> None:
    url = f"{DATABRICKS_INSTANCE}/api/2.0/secrets/list"
    response = requests.get(url, headers=HEADERS, params={"scope": scope_name})
    if response.status_code == 200:
        secrets = response.json().get("secrets", [])
        print(f"\n🔎 Secrets in scope '{scope_name}':")
        for secret in secrets:
            print(f" - 🔑 {secret['key']}")
    else:
        print(f"[❌] Failed to list secrets: {response.text}")

# 🔍 List ACLs (permissions) of the scope
def list_acls(scope_name: str) -> None:
    url = f"{DATABRICKS_INSTANCE}/api/2.0/secrets/acls/list"
    response = requests.get(url, headers=HEADERS, params={"scope": scope_name})
    if response.status_code == 200:
        acls = response.json().get("items", [])
        print(f"\n📜 ACLs for scope '{scope_name}':")
        for acl in acls:
            print(f" - 👤 {acl['principal']}: {acl['permission']}")
    else:
        print(f"[❌] Failed to list ACLs: {response.text}")

# ▶️ Execution
if __name__ == "__main__":
    create_scope(SCOPE_NAME)
    add_secrets(SCOPE_NAME, SECRETS)
    assign_acl(SCOPE_NAME, SP_NAME)
    list_secrets(SCOPE_NAME)
    list_acls(SCOPE_NAME)
