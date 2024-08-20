brand = str()
model = str()
type = ["1. Steer", "2. Pull", "3. Roll"]
state = tuple()
starting_odo = int()
serial = str()
conf = str()
tyre_db = []



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
        print("Unexpected value. Returning to start.")
        brand_create()    
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


#alternative coding for capturing tyre type. After practicing use of lists.
def type_create():
    type = ["1. Steer", "2. Pull", "3. Roll"]
    print(type)
    temp_type = int(input(f"Please select type from the above: (1/2/3)"))
    conf_type = (input(f"You have selected {type[temp_type-1]}. Is this correct? (y/n)"))
    if conf_type.lower() == 'y':
        print("Type Saved")
        temp_type = type[temp_type-1]
        return temp_type
    elif conf_type.lower() == 'n':
        type_create()
    else:
        print("Invalid selection. Please try again.")
        type_create()

def state_create():
    print("starting state create function")
    state = ["1. Virgin casing", "2. Second hand", "3. Retread", "4. Dud"]
    print(state)
    temp_state = int(input("Please select state from the above (1/2/3/4):   "))
    conf_state = input(f"You have selected {state[temp_state - 1]}. Is this correct? (y/n)")
    if conf_state.lower() == 'y':
        print("Type saved")
        return state[temp_state - 1]
    elif conf_state.lower() == 'n':
        state_create()
    else:
        print("Invalid selection. Please try again.")
        state_create()
    

def starting_create():
    starting_odo = get_latest_odo()
    #starting_odo = 0
    cust_conf = input(f"The default odo reading is {starting_odo}. Would you like to enter custom odo? (y/n)")
    if cust_conf.lower() == 'y':
        new_odo = int(input(f"Please enter new odo:  "))
        if (new_odo > 0) and (new_odo > starting_odo):
            starting_odo = new_odo
            print(f"{starting_odo} has been recorded as the starting odo of this tyre.")
            return starting_odo
        else:
            print("Custom odo reading cannot be lower than last known odo of truck")
            starting_create()
    elif cust_conf.lower() == 'n':
        return starting_odo
    else:
        print("Unexpected value. Please try again.")
        starting_create()    

    pass
    

#placeholder for function that takes fleet number of truck as arguement and return its latest known odo.
def get_latest_odo():
    print('This function will be used to fetch last known odo of a particular truck.')
    return 1234



#tyre_creation is intended to be used to add a tyre to the database of tyres and record its details.
#for the sake of simplicity I will only use a few attributes at first
#-brand - str
#-model - str
#-type - list
#-state - list
#-starting_odo (odometer reading at which lifespan of tyre starts) - int

def tyre_creation():
    print("Hello first function")
    new_tyre = {"Brand": "" , 
                "Model" : "",
                "Type" : "",
                "State" : "",
                "Start" : 0
                }
    
    new_tyre["Brand"] = brand_create()
    new_tyre["Model"] = model_create()
    new_tyre["Type"] = type_create()
    new_tyre["State"] = state_create()
    new_tyre["Start"] = starting_create()
    
    tyre_db.append(new_tyre)
    print(new_tyre)

        
main()