class Automobile():
    #define a constructor
    #the consstructor defines what happens when we create an automobile.
    def __init__(self, make, model, vin, engine_size, owner):
        #assign parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner