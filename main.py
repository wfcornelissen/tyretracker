brand = str()
model = str()
type = tuple["1. Steer", "2. Pull", "3. Roll"]
state = tuple()
starting_odo = int()
serial = str()
conf = str()



def main():
    print("Hello World")
    tyre_creation()
    
def brand_create():
    temp = input("Enter brand:")
    conf = input(f"You have entered {temp}. Is this correct? (y/n)")
    if conf.lower() == "y":
        print("Brand saved")
        brand = temp
    elif conf.lower() == "n":
        print("You selected no. Returning to start.")
        brand_create()
    else:
        print("Unexpected value. Exiting.")      
    return brand
def model_create():
    temp = input("Enter model:")
    conf = input(f"You have entered {temp}. Is this correct? (y/n)")
    if conf.lower() == "y":
        print("Model saved")
        model = temp
    elif conf.lower() == "n":
        print("You selected no. Returning to start.")
        brand_create()
    else:
        print("Unexpected value. Exiting.")
    return model
def type_create():
    type = ["1. Steer", "2. Pull", "3. Roll"]
    temp = int(input(f"Please choose type (1/2/3) {type}: "))
    print (f'you have selected {temp}')
    while temp != (1 or 2 or 3):
        print("Invalid selection")
        temp = input(f"Please choose type (1/2/3) {type}: ")
    conf = input(f"You have selected {type[(temp -1)]}. Is this correct? (y/n)")
    while conf != ("y" or "n"):
        print("Invalid selection")
        conf = input(f"You have selected {type[temp]}. Is this correct? (y/n)")
    if conf == "y":
        type = temp
    else:
        print("You selected no. Returning to start.")
        type_create()
    return type

    
#tyre_creation is intended to be used to add a tyre to the database of tyres and record its details.
#for the sake of simplicity I will only use a few attributes at first
#-brand - str
#-model - str
#-type - tuple
#-state - tuple
#-starting_odo (odometer reading at which lifespan of tyre starts) - int
def tyre_creation():
    print("Hello first function")
    #brand_create()
    #model_create()
    type_create()
     
        

        
main()