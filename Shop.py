class Bike:
    def __init__(self, id, wheels, company, inventory, riders=1):
        self.id = id
        self.wheels = int(wheels)
        self.company = company
        self.riders = int(riders)
        self.inventory = int(inventory)

    def get_company(self):
        return self.company

    def get_inventory(self):
        return self.inventory

    def rent(self, num_of_bikes):
        if int(num_of_bikes) <= self.inventory:
            self.inventory -= int(num_of_bikes)
            return True
        return False


    def __str__(self):
        return f"id:{self.id}, Num of Available Bikes:{self.inventory}, Company:{self.company}"

    def __eq__(self, other):
        return self.id == other.id and isinstance(other, Bike)

    def __hash__(self):
        return hash(self.id)


class Shop:
    def __init__(self, city="Tel Aviv", name="Rally"):
        self.name = name
        self.city = city
        self.bikes = dict()

    def add_bike(self, bike):
        if not isinstance(bike, Bike) or bike in self.bikes:
            return False
        if bike.get_inventory() <= 0:
            return False
        self.bikes[bike] = bike.get_inventory()
        return True
    def get_bikes_company(self):
        companies=[]
        for bike in self.bikes:
            companies.append(bike.get_company())
        return companies

    def check_available(self, num_of_bikes, bike):
        if int(num_of_bikes) > self.bikes[bike] or bike not in self.bikes:
            print("There are No Available Bikes")
            return False
        return True

    def take_bikes(self, num_of_bikes, bike):
        if not isinstance(bike, Bike):
            return False
        isRent=bike.rent(int(num_of_bikes))
        if isRent:
            self.bikes[bike]-=int(num_of_bikes)
        return False
    def calculate_rental_price(self, period, amount_of_time, bike,isCheckout=False, num_of_bikes=1):
        num_of_bikes=int(num_of_bikes)
        amount_of_time=int(amount_of_time)
        if not self.check_available(num_of_bikes, bike) or int(num_of_bikes) < 1:
            return False
        hour_price = 5
        day_price = 20
        week_price = 60
        period = str(period)
        num = int(amount_of_time)
        price = False
        if period.lower() == 'hourly':
            price = float(hour_price * num_of_bikes * num)
        elif period.lower() == 'daily':
            price = float(day_price * num_of_bikes * num)
        else:
            price = float(week_price * num_of_bikes * num)
        if 3 <= num_of_bikes <= 5:
            price = 0.7 * price
        if price != False and isCheckout==True:
            self.take_bikes(num_of_bikes, bike)
        return round(price,2)

    def find_by_company(self,company):
        for bike in self.bikes:
            if bike.company==company:
                return bike


    def __str__(self):
        back = "All bikes\n"
        back += '-' * 40 + "\n"
        for bike in self.bikes:
            back += f"{bike.__str__()}\n"
        return back


b1 = Bike(1, 2, "Trek", 30)
b2 = Bike(2, 3, "BMX", 2)
s = Shop()
s.add_bike(b1)
s.add_bike(b2)
print(s)
# print(s.calculate_rental_price('weekly', 2, b1, 2))
# print(s.calculate_rental_price('weekly', 2, s.find_by_company("BMX"),False, 2))
# print(s.calculate_rental_price('weekly', 2, s.find_by_company("BMX"),True, 1))
# print(s.bikes[b2])

# print(s.get_bikes_company())
# print(s.find_by_company("BMX"))


