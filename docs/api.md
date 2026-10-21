# API

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET` | `/health` | Health check |
| `POST` | `/pedidos` | Cria um pedido (status `criado`) |
| `GET` | `/pedidos/{id}` | Consulta um pedido |
| `PATCH` | `/pedidos/{id}/status?status=pago` | Atualiza o status |

## Exemplo

```bash
curl -X POST http://localhost:8080/pedidos \
  -H 'Content-Type: application/json' \
  -d '{"cliente_id": 7, "itens": ["caneta", "caderno"]}'
```

```json
{"cliente_id": 7, "itens": ["caneta", "caderno"], "id": 1, "status": "criado"}
```
