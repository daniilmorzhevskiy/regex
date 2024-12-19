#Manual testing --> E2E

"""def addition(a, b):
    return a+b


a = int(input("A: "))
b = int(input("B: "))

res = addition(a,b)
print(res)"""


#Problem: we want to test his function (Unit test)

"""
Test case 1 --> #Positive testing

Input: a = 10, b = 30

Expected res: 40

Test case 2 --> Negative testing

Input: a = str, b = float

Expected res: TypeError



"""
def addition(a:int, b:int) -> int:
    return a+b

#Only with part _test Pythhon can see that it is test
def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
