import pytest
from flask.backend.parser import Parser


parser = Parser()


def test_parser():
    assert parser.parser("ou est paris")[0] == "paris"
    assert parser.parser("Où est paRis")[0] == "paris"
    assert parser.parser("ou est la Tour EIFFEl")[0] == "la tour eiffel"
