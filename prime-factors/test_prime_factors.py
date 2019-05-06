from prime_factors import prime_factors

def test_factors_of_0():
    assert prime_factors(0) == []

def test_factors_of_2():
    assert prime_factors(2) == [2]

def test_factors_of_3():
    assert prime_factors(3) == [3]

def test_factors_of_10():
    assert prime_factors(10) == [2,5]

def test_factors_of_101():
    assert prime_factors(101) == [101]

def test_factors_of_315():
    assert prime_factors(315) == [3,3,5,7]

def test_factors_of_1024():
    assert prime_factors(315) == [2] * 10
