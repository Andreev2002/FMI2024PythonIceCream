#Singleton pattern
class IceCreamShop:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IceCreamShop, cls).__new__(cls)
            cls._instance.flavors = ["Vanilla", "Chocolate", "Strawberry"]
            cls._instance.addons = ["Chocolate Coating", "Chocolate Sprinkles"]
            cls._instance.customers = []
        return cls._instance

    def add_customer(self, customer):
        self.customers.append(customer)

    def notify_customers(self):
        for customer in self.customers:
            customer.update()
