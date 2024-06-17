from ice_cream_shop.ice_cream_shop import IceCreamShop
from ice_cream_shop.customer import Customer
from ice_cream_shop.ice_cream import IceCream
from ice_cream_shop.decorators import ChocolateCoating, ChocolateSprinkles
from ice_cream_shop.strategies import EatInPark

# Test code
shop = IceCreamShop()

customer1 = Customer("Atanas")
customer2 = Customer("Ivan")

shop.add_customer(customer1)
shop.add_customer(customer2)

shop.notify_customers()

plain_ice_cream = IceCream("Vanilla")
chocolate_coated_ice_cream = ChocolateCoating(plain_ice_cream)
fully_decorated_ice_cream = ChocolateSprinkles(chocolate_coated_ice_cream)

print(fully_decorated_ice_cream.get_description())
print(f"Total cost: ${fully_decorated_ice_cream.cost()}")

location_strategy = EatInPark()
location_strategy.eat(fully_decorated_ice_cream)
