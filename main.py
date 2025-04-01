
def sort(width: float, height: float, length: float, mass: float) -> str:
    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return 'Rejected'
    elif is_bulky or is_heavy:
        return 'Special'
    else:
        return 'Standard'

if __name__ == '__main__':
    sort(10, 10, 10, 5)

    # Standard case: not bulky, not heavy
    assert sort(10, 10, 10, 5) == 'Standard'  # volume = 1000, mass = 5
    # Bulky by dimension only
    assert sort(200, 10, 10, 5) == 'Special'  # width = 200
    # Bulky by volume only
    assert sort(100, 100, 100, 5) == 'Special'  # volume = 1,000,000
    # Heavy and bulky by volume
    assert sort(100, 100, 100, 25) == 'Rejected'  # volume = 1,000,000, mass = 25
