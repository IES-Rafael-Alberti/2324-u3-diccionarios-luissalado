from src.ejercicio2 import genera_mensaje


def test_genera_mensaje():
        assert genera_mensaje("John", "25", "1234567890", "123 Main St") == "John tiene 25 años, vive en 123 Main St y su numero de telefono es 1234567890"