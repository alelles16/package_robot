from robot import sort

assert sort(10, 10, 10, 5) == 'Standard'
assert sort(150, 10, 10, 5) == 'Special'
assert sort(10, 10, 10, 20) == 'Special'
assert sort(200, 100, 100, 25) == 'Rejected'

try:
    sort(-10, 10, 10, 5)
except ValueError as e:
    assert str(e) == "width is negative"

try:
    sort(10, None, 10, 5)
except ValueError as e:
    assert str(e) == "height is required"

try:
    sort("100", 10, 10, 5)
except TypeError as e:
    assert str(e) == "width is not numeric"
