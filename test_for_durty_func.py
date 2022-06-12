from schema import Schema
from functions import get_function

build_user = get_function()

schema = Schema({ # библиотека для проверки структуры словаря
    'email': str,
    'first_name': str,
    'last_name': str
})


def test_structure():
    schema.is_valid(build_user())


def test_random_data():
    assert build_user() != build_user()


def test_set_params():
    result_dict = build_user({'age': '22'})
    assert result_dict['age'] == '22'
    schema.is_valid(result_dict)
    
