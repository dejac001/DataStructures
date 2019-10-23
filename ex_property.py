class Celcius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8) + 32


class Celcius2:
    """Problem--everyone now has to change obj.temperature to obj._temperature"""
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature()*1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.:
            raise ValueError('Temperature below -273 is not possible!')
        self._temperature = value


class Celcius3:
    """Any code that retreives the value of temperature will
    automatically call get_temperature() instead of a dictionary
    __dict__ look-up. Similarly any code that assigns a value to temperature
    will automatically call set_temperature()"""
    def __init__(self, temperature = 0.):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8) + 32.

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273.:
            raise ValueError('Temperature below -273 is not possible')
        print("Setting value")
        self._temperature = value

    # use property, a built-in function that creates and returns a property object
    temperature = property(get_temperature, set_temperature)


class Celcius4:
    def __init__(self, temperature = 0.):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8) + 32.

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.:
            raise ValueError('Temperature below -273 is not possible')
        print("Setting value")
        self._temperature = value


def main():
    # c = Celcius3()
    c = Celcius4()
    c.temperature
    c.temperature = 37
    c.to_fahrenheit()


if __name__ == '__main__':
    main()