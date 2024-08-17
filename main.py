brand = str()
model = str()
type = ["1. Steer", "2. Pull", "3. Roll"]
state = tuple()
starting_odo = int()
serial = str()
conf = str()
tyre_db = {}



def main():
    print("Hello World")
    tyre_creation()



#function to receive and store the brand of a specific tyre
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

#function to receive and store the model of a specific tyre
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

#function to receive and store the type of a specific tyre
def type_create():
    type = ["1. Steer", "2. Pull", "3. Roll"]
    print(type)
    temp_type = int(input(f"Please select type from the above: "))
    print(temp_type)
    if temp_type == int(1):
        conf_type = str(input(f"You have selected 1. Steer. Is this correct? (y/n)"))
        if conf_type.lower() == "y":
            print("Type saved")
            type = conf_type
            return type
        else:
            type_create()
    elif temp_type == int(2):
        conf_type = str(input(f"You have selected 2. Pull. Is this correct? (y/n)"))
        if conf_type.lower() == "y":
            print("Type saved")
            type = conf_type
            return type
        else:
            type_create()
    elif temp_type == int(3):
        conf_type = str(input(f"You have selected 3. Roll. Is this correct? (y/n)"))
        if conf_type.lower() == "y":
            print("Type saved")
            type = conf_type
            return type
        else:
            type_create()
    else:
        print("Error: Input invalid.")
        type_create() 

    pass

    
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