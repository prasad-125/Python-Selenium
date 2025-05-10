import pytest

# @pytest.fixture()
@pytest .fixture(autouse=True,scope="session")     #function/session   #no need to mention method ex-setup
def setup():
    print("precondition")
    yield
    print("postcondition")


