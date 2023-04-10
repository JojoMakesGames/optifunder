
from project.functions import Object, check_fetch_input, check_set_input, fetch_param, set_param

# region set
def test_set_param_int():
    obj: Object = Object()
    obj = set_param(obj, 'a=1')
    assert obj.a == 1
    assert type(obj.a) == int

def test_set_param_bool():
    obj: Object = Object()
    obj = set_param(obj, 'a=True')
    assert obj.a == True
    assert type(obj.a) == bool

def test_set_param_str():
    obj: Object = Object()
    obj = set_param(obj, 'a=test')
    assert obj.a == 'test'
    assert type(obj.a) == str

def test_set_param_keeps_type():
    obj: Object = Object()
    obj = set_param(obj, 'a=1')
    error = check_set_input(obj, 'a=test')
    assert error != None
# endregion

# region fetch
def test_fetch_param(capsys):
    obj: Object = Object()
    setattr(obj, 'a', 1)
    obj = fetch_param(obj, 'a')
    captured = capsys.readouterr()
    assert captured.out.strip() == '1'

def fetch_param_keeps_type():
    obj: Object = Object()
    setattr(obj, 'a', 1)
    obj = fetch_param(obj, 'a')
    assert type(obj.a) == int

def test_fetch_param_not_found(capsys):
    obj: Object = Object()
    obj = fetch_param(obj, 'a')
    captured = capsys.readouterr()
    # This seems like there could be more built out to make it not fragile if you wanted another error
    assert captured.out.strip() == 'Parameter a not found.'

def test_fetch_param_all(capsys):
    obj: Object = Object()
    setattr(obj, 'a', 1)
    setattr(obj, 'b', 2)
    setattr(obj, 'c', 3)
    obj = fetch_param(obj, '*')
    captured = capsys.readouterr()
    assert captured.out == 'a 1\nb 2\nc 3\n'

def test_fetch_param_no_input():
    obj: Object = Object()
    error = check_fetch_input(obj, '')
    assert error is not None
# endregion

    

