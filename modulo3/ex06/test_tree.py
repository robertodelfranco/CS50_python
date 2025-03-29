from arvore_genealogica import encontrar_ancestrais

familia_silva = {
	"João": {
	"pais": ["Maria", "Pedro"],
	"nascimento": 1980,
	"cidade": "São Paulo"
	},
	"Maria": {
	"pais": ["Ana", "Carlos"],
	"nascimento": 1955,
	"cidade": "Rio de Janeiro"
	},
	"Pedro": {
	"pais": ["Beatriz", "José"],
	"nascimento": 1953,
	"cidade": "Belo Horizonte"
	},
	"Ana": {
	"pais": ["Francisca", "Antônio"],
	"nascimento": 1930,
	"cidade": "Salvador"
	},
	"Carlos": {
	"pais": [],
	"nascimento": 1928,
	"cidade": "Recife"
	},
	"Beatriz": {
	"pais": ["Helena", "Manuel"],
	"nascimento": 1925,
	"cidade": "Fortaleza"
	},
	"José": {
	"pais": [],
	"nascimento": 1923,
	"cidade": "Porto Alegre"
	}
}


def test_find_none():
	given = encontrar_ancestrais(familia_silva, "matheus")
	expected = []
	assert expected == given

def test_find_ancestral_ana():
	given = encontrar_ancestrais(familia_silva, "Ana")
	expected = ['Francisca', 'Antônio']
	assert expected == given

def test_find_ancestral_maria():
	given = encontrar_ancestrais(familia_silva, "Maria")
	expected = ['Ana', 'Carlos', 'Francisca', 'Antônio']
	assert expected == given

def test_find_ancestral_joao():
	given = encontrar_ancestrais(familia_silva, "João")
	expected = ['Maria', 'Pedro', 'Ana', 'Carlos', 'Beatriz', 'José', 'Francisca', 'Antônio', 'Helena', 'Manuel']
	assert expected == given