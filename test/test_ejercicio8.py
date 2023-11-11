from src.ejercicio8 import frase

def test_create_dictionary(monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda _: 'casa:house,perro:dog')
        frase()
        captured = capsys.readouterr()
        assert captured.out == "\nDiccionario creado:\n{'casa': 'house', 'perro': 'dog'}\n"