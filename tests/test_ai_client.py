from unittest.mock import patch
from ai_cliente import gerar_frase_motivacional

@patch("ai_cliente.requests.post")
def test_gerar_frase_motivacional(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = [
        {"generated_text": "Acredite no seu foco e tudo será possível!"}
    ]

    tema = "foco"
    frase = gerar_frase_motivacional(tema)

    assert isinstance(frase, str)
    assert len(frase) > 0
    assert "foco" in frase.lower() or "acredite" in frase.lower()