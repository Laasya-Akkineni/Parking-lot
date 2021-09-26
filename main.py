file = open("input.py")
contents = file.read()
file.close()
list_input_commands = list(contents.split("\n"))
for i in range(len(list_input_commands)):
    if "Create" in list_input_commands[i]:
        parking_slots =int(list_input_commands[i][-1]) 
        list_vehicle_numbers = []
        list_drivers_age = []
        print("Created parking of " + str(list_input_commands[i][-1]) + " slots ")
    if len(list_vehicle_numbers)==parking_slots:
      print("The parking lot is full.Please wait for sometime util  any slot is free.Sorry for the inconvenience caused!!!")
      break   
    elif "Park" in list_input_commands[i] :
        if "" in list_vehicle_numbers:
            idx = list_vehicle_numbers.index("")
            list_vehicle_numbers[idx] = list_input_commands[i][5:18]
            list_drivers_age[idx] = int(list_input_commands[i][-2:])
        else:
            list_vehicle_numbers.append(list_input_commands[i][5:18])
            list_drivers_age.append(int(list_input_commands[i][-2:]))

        print("Car with vehicle registration number " + '"' + str(list_input_commands[i][5:18]) +'"' + " has been parked at slot number " +
              str(list_vehicle_numbers.index(list_input_commands[i][5:18]) + 1))
        
    if "Slot" in list_input_commands[i]:
        if "driver" in list_input_commands[i]:
            driver_age = int(list_input_commands[i][-2:])
            count_of_drivers = []
            for i in range(len(list_drivers_age)):
                if list_drivers_age[i] == driver_age:
                    count_of_drivers.append(i + 1)
            print(",".join(str(i) for i in count_of_drivers))

        else:
            c = "".join(list_input_commands[i][-13:])
            print(list_vehicle_numbers.index(c) + 1)
    if "Leave" in list_input_commands[i]:
        print("Slot number " + str(list_input_commands[i][-1]) + " vacated, the car with vehicle registration number " + '"' +list_vehicle_numbers[int(list_input_commands[i][-1]) - 1] + '"' +" left the space, the driver of the car was of age " +str(list_drivers_age[int(list_input_commands[i][-1]) - 1]))
        list_vehicle_numbers[int(list_input_commands[i][-1]) - 1] = ""
        list_drivers_age[int(list_input_commands[i][-1]) - 1] = 0
