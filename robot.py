from package import Package

def sort(width: float, height: float, length: float, mass: float) -> str:
    pkg = Package(width, height, length, mass)
    return pkg.classify()

if __name__ == "__main__":
    print(sort(100, 100, 100, 5))  # Special
    print(sort(10, 10, 10, 5))  # Standard
    print(sort(150, 150, 150, 25))  # Rejected
