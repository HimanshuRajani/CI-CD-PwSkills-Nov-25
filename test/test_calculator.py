from App.calculator import add,sub

def test_add():
  assert add(5,9) == 14

def test_sub():
  assert sub(10,8) == 2
