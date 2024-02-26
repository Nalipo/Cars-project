class Engine:
    def __init__(self, capacity):
            self.capacity = capacity

    def start_engine(self):
        if int(self.capacity) <= 0:
            print('Несуществующая машина')
        else:
            print(f"Engine({self.capacity}) started")

    def accelerate(self):
        print(f"Accelerating({self.capacity}) the engine")

    def stop_engine(self):
        print(f"Engine({self.capacity}) stopped")


class Car:
    def __init__(self, make, model, capacity):
        self.make = make
        self.model = model
        self.engine = Engine(capacity=capacity)

    def start(self):
        print(f"Starting the {self.make} {self.model}")
        self.engine.start_engine()

    def drive(self):
        print(f"Driving the {self.make} {self.model}")
        self.engine.accelerate()

    def stop(self):
        print(f"Stopping the {self.make} {self.model}")
        self.engine.stop_engine()


# Создаем объекты классов и демонстрируем взаимодействие
my_car = Car("Toyota", "Camry", "2000")
my_car.start()
my_car.drive()
my_car.stop()
