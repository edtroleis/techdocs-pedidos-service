from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Pedidos API", version="0.1.0")


class Status(str, Enum):
    criado = "criado"
    pago = "pago"
    enviado = "enviado"
    entregue = "entregue"
    cancelado = "cancelado"


class PedidoIn(BaseModel):
    cliente_id: int
    itens: list[str]


class Pedido(PedidoIn):
    id: int
    status: Status = Status.criado


_pedidos: dict[int, Pedido] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/pedidos", status_code=201)
def criar_pedido(data: PedidoIn) -> Pedido:
    pedido = Pedido(id=len(_pedidos) + 1, **data.model_dump())
    _pedidos[pedido.id] = pedido
    return pedido


@app.get("/pedidos/{pedido_id}")
def obter_pedido(pedido_id: int) -> Pedido:
    if pedido_id not in _pedidos:
        raise HTTPException(status_code=404, detail="pedido não encontrado")
    return _pedidos[pedido_id]


@app.patch("/pedidos/{pedido_id}/status")
def atualizar_status(pedido_id: int, status: Status) -> Pedido:
    pedido = obter_pedido(pedido_id)
    pedido.status = status
    return pedido
