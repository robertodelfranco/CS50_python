# import pytest
from read_file import readfile


def test_readfile(tmp_path):
	arquivo_teste = tmp_path / "teste.txt"
	conteudo_esperado = "Olá, mundo! everything is okay?"
	arquivo_teste.write_text(conteudo_esperado, encoding="utf-8")

	with arquivo_teste.open("r", encoding="utf-8") as f:
		conteudo_lido = readfile(f)
    
	assert conteudo_lido == conteudo_esperado
