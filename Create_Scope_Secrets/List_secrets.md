# 🔐 Comandos Databricks CLI – Secrets & Scopes

## ✅ Listar os secrets dentro de um Secret Scope

```bash
databricks secrets list-secrets <you scope>
```

---

## ✅ Listar todos os Secret Scopes existentes

```bash
databricks secrets list-scopes
```

---

## ✅ Listar permissões (ACLs) de um Secret Scope

```bash
databricks secrets list-acls <you scope>
```

---

## 🧠 Dica: Usando perfis específicos

Se estiver utilizando múltiplos perfis configurados no `~/.databrickscfg`, utilize a flag `--profile` para especificar qual perfil deve ser usado:

```bash
databricks secrets list-secrets minai_secrets --profile <you-profile>
```
