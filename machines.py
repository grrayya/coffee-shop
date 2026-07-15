class BrewingUnit:
    def __init__(self):
        self.water = 1000

    def brew_espresso(self):
        if self.water < 30:
            raise RuntimeError("Refill water tank before brewing")
        self.water -= 30
        return "Espresso Shot"
