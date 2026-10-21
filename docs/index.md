# Pedidos Service

Recebe e acompanha pedidos de clientes, do momento em que são criados até a entrega.

| | |
|---|---|
| **Owner** | `platform-team` |
| **System** | `demo-system` |
| **Tipo** | service |
| **Linguagem** | Python 3.14 · FastAPI |

!!! tip "Esta doc foi criada seguindo o guia da aba TechDocs"
    O serviço nasceu sem documentação. O guia que aparece na aba TechDocs de componentes sem doc
    foi seguido passo a passo, e o resultado é esta página. Compare com o
    [Pagamentos Service](http://localhost:3000/catalog/default/component/pagamentos-service/docs),
    que ainda não tem docs.

## Como rodar localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8080
```

Swagger em <http://localhost:8080/docs>.

## Próximos passos

- [Arquitetura](arquitetura.md): ciclo de vida do pedido e dependências.
- [API](api.md): endpoints e exemplos.
- [Runbook](runbook.md): operação e troubleshooting.
