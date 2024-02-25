#########################################################################################
# Find all numbers less than 100 where the sum of the digits is divisible by 7
#########################################################################################

#========================================================================================
# Without functions
#========================================================================================

y = [xx for xx in range(100) if ((xx // 10) + (xx % 10)) % 7 == 0]

#========================================================================================
# With functions
#========================================================================================

def tens(x):
	return x // 10

def ones(x):
	return x % 10

def sum_digits(x):
	return tens(x) + ones(x)

def is_divisible(x, divisor):
	return x % divisor == 0

z = [xx for xx in range(100) if is_divisible(sum_digits(xx), 7)]


# Verify the results are the same
def test_verify_results():
	assert y == z

#========================================================================================
# Tests for functions
#========================================================================================

def test_tens():
    assert tens(0) == 0
    assert tens(5) == 0
    assert tens(10) == 1
    assert tens(42) == 4
    assert tens(123) == 2
  
def test_ones():
    assert ones(0) == 0
    assert ones(5) == 5
    assert ones(10) == 0
    assert ones(42) == 2
    assert ones(123) == 3
  
def test_sum_digits():
    assert sum_digits(0) == 0
    assert sum_digits(5) == 5
    assert sum_digits(10) == 1
    assert sum_digits(42) == 6
    assert sum_digits(123) == 6
