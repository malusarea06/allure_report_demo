import pytest
import allure

def test_methA():
    allureLogs("Launch Test")
    print("This is method A")

def test_methB():
    print("This is method B")
    allureLogs("This is method B")

def test_methC():
    print("This is method C")
    assert 1==2

def test_methD():
    print("This is method D")

def allureLogs(text):
    with allure.step(text):
        pass
