class BrewingUnit:
    def __init__(self):
        self.water = 1000

    def brew(self):
        if self.water < 30:
            raise RuntimeError("Water tank empty")
        self.water -= 30
        return "Espresso Shot"
