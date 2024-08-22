#this code will record the fleet's truck details and output them to a csv file.
#-reg
#-VIN
#-axle info
#-make
#-model
#-year
#-finance?
#-R&M
#-latest odo
#-record of faults

def truck_capture():
    print("Hello truck_capture")
    reg_capture()
    #vin_capture()
    #axle_info_capture()
    #make_capture()
    #model_capture()
    #year_capture()
    #finance_capture()
    #rnm_capture()
    #latest_odo_capture()
    #record_of_faults()


def reg_capture():
    reg_temp = input("Please enter truck registration number:  ")
    conf = input(f"You have input {reg_temp}. Is this correct? (y/n):  ")
    if conf.lower() == 'y':
        return reg_temp
    elif conf.lower() == 'n':
        reg_capture()
    else:
        print("Invalid input. Please try again.")
        reg_capture()
    

def vin_capture():
    print("Hello vin_capture")

def axle_info_capture():
    print("Hello axle_info_capture")

def make_capture():
    print("Hello make_capture")

def model_capture():
    print("Hello model_capture")

def year_capture():
    print("Hello year_capture")

def finance_capture():
    print("Hello finance_capture")

def rnm_capture():
    print("Hello rnm_capture")

def latest_odo_capture():
    print("Hello latest_odo_capture")

def record_of_faults():
    print("Hello record_of_faults")


truck_capture()