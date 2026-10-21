# Arquitetura

## Ciclo de vida do pedido

```mermaid
stateDiagram-v2
    direction LR
    [*] --> criado : POST /pedidos
    criado --> pago : pagamento autorizado
    criado --> cancelado : cliente cancela
    pago --> enviado : separado no estoque
    enviado --> entregue : confirmação da transportadora
    entregue --> [*]
    cancelado --> [*]
```

*Figura 1 · Status possíveis de um pedido e o que dispara cada transição.*

## Dependências

```mermaid
flowchart LR
    cliente([Cliente]):::canal -- HTTP/JSON --> pedidos[Pedidos Service]:::servico
    pedidos -- autoriza pagamento --> pagamentos[Pagamentos Service]:::servico
    pedidos --> db[(Pedidos · memória)]:::dados

    classDef canal fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a
    classDef servico fill:#dcfce7,stroke:#22c55e,color:#14532d
    classDef dados fill:#f3e8ff,stroke:#a855f7,color:#581c87
```

*Figura 2 · O Pedidos Service depende do Pagamentos Service para autorizar o pagamento.*

!!! warning "PoC"
    O armazenamento é em memória e os pedidos se perdem a cada restart.
