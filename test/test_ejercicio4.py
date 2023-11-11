from unittest.mock import patch
from src.ejercicio4 import fecha_input


def test_fecha_imput():

        input_values = ['01/01/2022']

        with patch('builtins.input', side_effect=input_values):
            fecha_input()

