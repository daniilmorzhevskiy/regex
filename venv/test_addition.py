from tests import addition

#Only with part _test Pythhon can see that it is test
def test_add():
    assert addition(2, 3) == 5
    assert addition('space', 'ship') == 'spaceship'