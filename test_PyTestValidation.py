#fixtures - reusable code for setup and teardown
import pytest

@pytest.fixture(scope='module') #scope can be 'function', 'class', 'module', or 'session'
def preWork():
    print("This is the pre-work for the functions.")
    return "pass"

@pytest.fixture(scope='module') #scope can be 'function', 'class', 'module', or 'session'
def secondWork():
    print("I set up the second work for the functions.")
    yield
    print("Tear down validation")

def test_initialcheck(preWork,secondWork):
    print("This is the initial check for pytest validation.")
    noTest()
    assert preWork == "pass"

def test_2initialcheck(preWork,secondWork):
    print("This is the 2 initial check for pytest validation.")

def test_secondcheck(preSetupWork, secondWork):
    print("This is the secound check for pytest validation.")

def noTest():
    print("This is not a test function, it should not be executed.")
