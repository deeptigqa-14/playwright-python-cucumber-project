import pytest


@pytest.fixture(scope="session")
def usercredentials(request): #request access global variable and local variable
    return request.param
