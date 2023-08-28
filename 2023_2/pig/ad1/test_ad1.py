import pytest

from ad1 import CampoMinado

# Teste para a função gerar minas

def test_gerar_minas():
    tamanho = 3
    minas = 3
    jogo = CampoMinado(tamanho, minas)

    # Conta minas no campo gerado
    minas_count = sum(row.count(-1) for row in jogo.mapa)
    
    assert minas_count == minas

# Teste para a função atualizar vizinhos

def test_atualizar_vizinhos():
    tamanho = 3
    minas = 1
    jogo = CampoMinado(tamanho, minas)

    # Checa se os vizinhos da mina foram atualizados
    x, y = 0, 0
    vizinhos = [(0, 1), (1, 0), (1, 1)]
    vizinhos_values = [jogo.mapa[i][j] for i, j in vizinhos]
    assert (value == -1 for value in vizinhos_values)


# Teste para a função revelar

def test_revelar():
    tamanho = 3
    minas = 0
    jogo = CampoMinado(tamanho, minas)

    # Teste revelando uma célula com valor 0 deve revelar recursivamente vizinhos.
    jogo.revelar(0, 0)
    revealedo_count = sum(row.count(True) for row in jogo.revelado)
    assert revealedo_count == 9  # Todas as células devem ser reveladas

# Teste de condições de vencer

def test_condicoes_vencer():
    tamanho = 2
    minas = 1
    jogo = CampoMinado(tamanho, minas)

    x, y = 0, 0
    # Revele a célula segura
    jogo.revelar(1, 1)
    jogo.revelar(x, y)

    assert (all(revealed for revealed in linha) for linha in jogo.revelado)

# pytest -s test_ad1_2023_2.py
if __name__ == "__main__":
    pytest.main()