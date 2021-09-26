f = open("input.py")
contents = f.read()
f.close()
l = list(contents.split("\n"))
for i in range(len(l)):
    if "Create" in l[i]:
        parking_lot =int(l[i][-1]) 
        list_vehicle_numbers = []
        list_drivers_age = []
        print("Created parking of " + str(l[i][-1]) + " slots ")
    if len(list_vehicle_numbers)==parking_lot:
      print("The parking lot is full.Please wait for sometime util other any slot is empty.Sorry for the inconvineince!!!")
      break   
    if "Park" in l[i] :
        if "" in list_vehicle_numbers:
            idx = list_vehicle_numbers.index("")
            list_vehicle_numbers[idx] = l[i][5:18]
            list_drivers_age[idx] = int(l[i][-2:])
        else:
            list_vehicle_numbers.append(l[i][5:18])
            list_drivers_age.append(int(l[i][-2:]))

        print("Car with vehicle registration number " + '"' + str(l[i][5:18]) +'"' + " has been parked at slot number " +
              str(list_vehicle_numbers.index(l[i][5:18]) + 1))
        
    if "Slot" in l[i]:
        if "driver" in l[i]:
            d = int(l[i][-2:])
            dl = []
            for i in range(len(list_drivers_age)):
                if list_drivers_age[i] == d:
                    dl.append(i + 1)
            print(",".join(str(i) for i in dl))

        else:
            c = "".join(l[i][-13:])
            print(list_vehicle_numbers.index(c) + 1)
    if "Leave" in l[i]:
        print("Slot number " + str(l[i][-1]) + " vacated, the car with vehicle registration number " + '"' +list_vehicle_numbers[int(l[i][-1]) - 1] + '"' +" left the space, the driver of the car was of age " +str(list_drivers_age[int(l[i][-1]) - 1]))
        list_vehicle_numbers[int(l[i][-1]) - 1] = ""
        list_drivers_age[int(l[i][-1]) - 1] = 0
