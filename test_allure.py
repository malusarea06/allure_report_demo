import pytest
import allure

def test_methA():
    allureLogs("Launch Test")
    print("This is method A")

def test_methB():
    print("This is method B")
    allureLogs("This is method B")

@pytest.mark.skip
def test_methC():
    print("This is method C")
    assert False

def test_methD():
    print("This is method D")

def allureLogs(text):
    with allure.step(text):
        pass
