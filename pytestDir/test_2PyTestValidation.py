#fixtures - reusable code for setup and teardown
import pytest


@pytest.mark.smoke
def test_thirdcheck(preSetupWork):
    print("This is the third check for pytest validation.")