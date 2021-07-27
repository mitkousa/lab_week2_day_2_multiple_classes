class BusStop:
    def __init__(self, bus_stop):
        self.bus_stop = bus_stop
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)
