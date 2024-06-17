#Strategy pattern
from ice_cream_shop.ice_cream import IceCream

class EatingLocationStrategy:
    def eat(self, ice_cream):
        pass

class EatInShop(EatingLocationStrategy):
    def eat(self, ice_cream):
        print(f"Enjoying {ice_cream.get_description()} in the shop.")

class EatInPark(EatingLocationStrategy):
    def eat(self, ice_cream):
        print(f"Enjoying {ice_cream.get_description()} in the park.")

class EatAtBeach(EatingLocationStrategy):
    def eat(self, ice_cream):
        print(f"Enjoying {ice_cream.get_description()} at the beach.")
