import pytest

def test_listar_produtos_quando_banco_esta_vazio(client):
    """Requisito 4.3a: Listar produtos quando o banco está vazio."""
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json() == []

def test_criar_produto_e_verificar_que_aparece_na_listagem(client):
    """Requisito 4.3c: Criar produto e verificar que aparece na listagem."""
    payload = {"nome": "Teclado Mecânico", "preco": 350.00, "descricao": "RGB Switch Blue", "ativo": True}
    
    post_res = client.post("/produtos", json=payload)
    assert post_res.status_code == 201
    
    get_res = client.get("/produtos")
    assert get_res.status_code == 200
    produtos = get_res.json()
    assert len(produtos) == 1
    
    map_produto = produtos[0]["nome"]
    assert map_produto == "Teclado Mecânico"



def test_criar_produto_e_verificar_persistencia(client):
    """Requisito 4.3b: Criar produto e verificar persistência no banco."""
    payload = {"nome": "Mouse Gamer", "preco": 200.00, "descricao": "16000 DPI", "ativo": True}
    response = client.post("/produtos", json=payload)
    
    assert response.status_code == 201
    dados = response.json()
    assert "id" in dados
    assert dados["nome"] == "Mouse Gamer"


def test_buscar_produto_por_id_sucesso(client, produto_existente):
    """Requisito 4.3d: Buscar produto por id — caso de sucesso."""
    id_produto = produto_existente["id"]
    response = client.get(f"/produtos/{id_produto}")
    
    assert response.status_code == 200
    assert response.json()["nome"] == "Monitor UltraWide"

def test_buscar_produto_com_id_inexistente_retorna_404(client):
    """Requisito 4.3e: Buscar produto com id inexistente — deve retornar 404."""
    response = client.get("/produtos/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado."



def test_deletar_produto_sucesso(client, produto_existente):
    """Requisito 4.3f: Deletar produto — deve retornar 204."""
    id_produto = produto_existente["id"]
    response = client.delete(f"/produtos/{id_produto}")
    assert response.status_code == 204

def test_deletar_produto_e_confirmar_remocao_com_get(client, produto_existente):
    """Requisito 4.3g: Deletar produto e confirmar remoção com GET subsequente."""
    id_produto = produto_existente["id"]
    
    del_res = client.delete(f"/produtos/{id_produto}")
    assert del_res.status_code == 204
    
    get_res = client.get(f"/produtos/{id_produto}")
    assert get_res.status_code == 404

def test_deletar_produto_inexistente_retorna_404(client):
    """Requisito 4.3h: Deletar produto inexistente — deve retornar 404."""
    response = client.delete("/produtos/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado."



def test_validar_isolamento_de_estado_entre_execucoes(client):
    """Requisito 4.3j: Teste que valide que o banco está isolado entre execuções."""

    response = client.get("/produtos")
    assert response.status_code == 200
    assert len(response.json()) == 0

@pytest.mark.parametrize(
    "payload_invalido",
    [

        {"nome": "Fone", "ativo": True},    
        {"preco": 150.0, "ativo": True}     
    ]
)
def test_criar_produto_payload_invalido_retorna_422(client, payload_invalido):
    response = client.post("/produtos", json=payload_invalido)
    assert response.status_code == 422