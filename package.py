class Package:

    def __init__(self, width: float, height: float, length: float, mass: float):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass
        self._validate_inputs()

    def _validate_inputs(self):
        attrs = {'width': self.width, 'height': self.height, 'length': self.length, 'mass': self.mass}
        for name, value in attrs.items():
            if value is None:
                raise ValueError('{} is required'.format(name))
            if not isinstance(value, (int, float)):
                raise TypeError('{} is not numeric'.format(name))
            if value < 0:
                raise ValueError('{} is negative'.format(name))

    def is_bulky(self) -> bool:
        volume = self.width * self.height * self.length
        return (
            volume >= 1_000_000 or
            self.width >= 150 or
            self.height >= 150 or
            self.length >= 150
        )

    def is_heavy(self) -> bool:
        return self.mass >= 20

    def classify(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()
        if bulky and heavy:
            return 'Rejected'
        elif bulky or heavy:
            return 'Special'
        return 'Standard'
