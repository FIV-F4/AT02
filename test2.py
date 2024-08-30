import pytest
from main import *

@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()

def test_add_or_get_user(db_conn):

    add_user(db_conn, 'Ivan', 20)
    user = get_users(db_conn, 'Ivan')
    assert user == (1, 'Ivan', 20)





def test_check():

    assert check(2) == True

def test_check2():
    assert check(3) == False

@pytest.mark.parametrize("number, expected", [(2, True), (3, False),(0, True), (55, False), (-77, False)])

def test_check_with_params(number, expected):
    assert check(number) == expected

def test_is_polindrom():
    assert is_polindrom(121) == True

def test_is_polindrom_false():
    assert is_polindrom(123) == False

@pytest.mark.parametrize("number, expected", [('level', True), ('python', False),('racecar', True), ('', True)])

def test_is_polindrom_with_params(number, expected):
    assert is_polindrom(number) == expected


def test_sort_list():
    assert sort_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]



