#decorator pattern
from ice_cream_shop.ice_cream import IceCream

class AddonDecorator(IceCream):
    def __init__(self, ice_cream):
        self.ice_cream = ice_cream

    def get_description(self):
        return self.ice_cream.get_description()

    def cost(self):
        return self.ice_cream.cost()

class ChocolateCoating(AddonDecorator):
    def get_description(self):
        return f"{self.ice_cream.get_description()} with Chocolate Coating"

    def cost(self):
        return self.ice_cream.cost() + 0.5

class ChocolateSprinkles(AddonDecorator):
    def get_description(self):
        return f"{self.ice_cream.get_description()} with Chocolate Sprinkles"

    def cost(self):
        return self.ice_cream.cost() + 0.3
