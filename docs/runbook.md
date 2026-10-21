# Runbook

## Health check

```bash
curl -s http://localhost:8080/health
# {"status":"ok"}
```

## Problemas comuns

??? question "404 em um pedido que acabei de criar"
    O armazenamento é em memória: se o processo reiniciou, os pedidos foram perdidos.

??? question "422 ao atualizar o status"
    O status precisa ser um destes: `criado`, `pago`, `enviado`, `entregue`, `cancelado`.

## Escalonamento

Time dono: `platform-team`. Dúvidas ou correções nesta doc: botão **Comentar** no topo da página.
