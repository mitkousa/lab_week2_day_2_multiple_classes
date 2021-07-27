class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return  len(self.queue)

    def clear(self):
        self.queue.clear()

    # reduce amount in persons cash
    # increase bus amount
    # decrease bus seats
    # remove from queue

    def get_on_bus(self, person, bus):
        person.pay_fare(bus)
        bus.receive_fare
        bus.capacity