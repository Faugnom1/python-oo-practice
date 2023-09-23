"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting value."""
        self.start = start
        self.current = start

    def generate(self):
        """Generate the next serial number in the sequence."""
        serial_number = self.current
        self.current += 1
        return serial_number      

    def reset(self):
        """Reset the generator to the initial value."""
        self.current = self.start


serial = SerialGenerator(start=100)
print serial.generate()