from series.series import fibonacci, lucas, sum_series

def test_fibonacci1():
    expected = 0
    actual = fibonacci(1)
    assert actual == expected

def test_fibonacci2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fibonacci3():
    expected = 1
    actual = fibonacci(3)
    assert actual == expected

def test_fibonacci4():
    expected = 2
    actual = fibonacci(4)
    assert actual == expected


def test_fibonacci5():
    expected = 3
    actual = fibonacci(5)
    assert actual == expected

def test_fibonaccinegative():
    expected = None
    actual = fibonacci(-3)
    assert actual == expected

def test_lucas1():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas2():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas3():
    expected = 3
    actual = lucas(2)
    assert actual == expected

def test_lucas4():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_lucas5():
    expected = 7
    actual = lucas(4)
    assert actual == expected

def test_lucas11():
    expected = 11
    actual = lucas(5)
    assert actual == expected

# Tests for sum_series function with Fibonacci sequence
def test_sum_series_fibonacci1():
    expected = 0
    actual = sum_series(0)
    assert actual == expected

def test_sum_series_fibonacci2():
    expected = 1
    actual = sum_series(1)
    assert actual == expected

def test_sum_series_fibonacci3():
    expected = 2
    actual = sum_series(3)
    assert actual == expected

def test_sum_series_fibonacci4():
    expected = 21
    actual = sum_series(8)
    assert actual == expected

def test_sum_series_fibonacci5():
    expected = 144
    actual = sum_series(12)
    assert actual == expected


# Tests for sum_series function with Lucas sequence
def test_sum_series_lucas1():
    expected = 2
    actual = sum_series(0, 2, 1)
    assert actual == expected

def test_sum_series_lucas2():
    expected = 1
    actual = sum_series(1, 2, 1)
    assert actual == expected

def test_sum_series_lucas3():
    expected = 3
    actual = sum_series(2, 2, 1)
    assert actual == expected

def test_sum_series_lucas4():
    expected = 11
    actual = sum_series(5, 2, 1)
    assert actual == expected

def test_sum_series_lucas5():
    expected = 29
    actual = sum_series(7, 2, 1)
    assert actual == expected


