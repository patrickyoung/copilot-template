# test_config.py
import pytest
from app import create_app

def test_config():
    """ Test if the configuration is loaded properly. """
    app = create_app()
    assert app is not None
