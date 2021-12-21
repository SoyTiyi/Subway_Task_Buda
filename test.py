import pytest
from Subway import Subway

@pytest.fixture
def subway():
    sub = Subway()
    return sub

def test_input_green(subway):
    assert "['a', 'b', 'c', 'd', 'e', 'f']" ==  str(subway.handleInput("input.txt","a","f","green"))

def test_input_green_error(subway):
    try:
        subway.handleInput("input.txt","a","h","green")
        assert(False)
    except:
        assert(True)

def test_input_red(subway):
    assert "['a', 'b', 'c', 'h', 'f']" ==  str(subway.handleInput("input.txt","a","f","red"))

def test_input_red_error(subway):
    try:
        subway.handleInput("input.txt","a","i","red")
        assert(False)
    except:
        assert(True)

def test_input_two_green(subway):
    assert "['a', 'c', 'g', 'i']" ==  str(subway.handleInput("input_two.txt","a","i","green"))

def test_input_two_green_error(subway):
    try:
        subway.handleInput("input_two.txt","a","i","red")
        assert(False)
    except:
        assert(True)

def test_input_two_red(subway):
    assert "['a', 'b', 'c', 'h', 'f']" ==  str(subway.handleInput("input_two.txt","a","f","red"))

def test_input_two_red_error(subway):
    try:
        subway.handleInput("input_two.txt","a","f","green")
        assert(False)
    except:
        assert(True)

def test_input_three_green(subway):
    assert "['a', 'c', 'e', 'i', 'g']" ==  str(subway.handleInput("input_three.txt","a","g","green"))

def test_input_three_green_error(subway):
    try:
        subway.handleInput("input_three.txt","a","g","red")
        assert(False)
    except:
        assert(True)

def test_input_three_red(subway):
    assert "['b', 'd', 'f', 'h']" ==  str(subway.handleInput("input_three.txt","b","h","red"))

def test_input_three_red_error(subway):
    try:
        subway.handleInput("input_three.txt","b","h","green")
        assert(False)
    except:
        assert(True)