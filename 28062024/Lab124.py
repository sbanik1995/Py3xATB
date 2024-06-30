class Car:
    name = None
    make = None
    model = None


    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a new car with the name:" + self.name)
        print("Starting a new car with the make:" + self.make)
        print("Starting a new car with the model:" + self.model)


lambo  = Car(" lambo ", " V2 " , " 2024 " )
lambo.start_engine()


xuv = Car(" xuv ", " V2 ", " 2024 ")
xuv.start_engine()
