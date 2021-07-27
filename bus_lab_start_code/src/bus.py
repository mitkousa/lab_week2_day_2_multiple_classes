class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
        self.amount = 0
        self.seats = capacity

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passengers.extend(bus_stop.queue)
        bus_stop.clear

    def remaining_capacity(self):
        return self.capacity

    def receive_fare(self):
        self.amount += self.price

    def remaining_seats(self):
        self.seats -= len(self.passengers)