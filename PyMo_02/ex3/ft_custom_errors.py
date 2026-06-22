def GardenError(Exception):
    def __init__(self, message, errors):
        super.__init__(message)
        if not errors:
            self.errors = "Unknown plant error"
        else:
            self.errors = errors


print("=== Custom Garden Errors Demo ===")
