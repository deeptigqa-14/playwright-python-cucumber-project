import pytest


@pytest.fixture(scope='session') #scope can be 'function', 'class', 'module', or 'session'
def preSetupWork():
    print("This is the pre-work for the session.")