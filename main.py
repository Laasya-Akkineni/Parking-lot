f = open("input.py")
contents = f.read()
f.close()
l = list(contents.split("\n"))
for i in range(len(l)):
    if "Create" in l[i]:
        plot = [0 for i in range(int(l[i][-1]))]
        ci = []
        di = []
        print("Created parking of " + str(l[i][-1]) + " slots ")
    if len(ci)==len(plot):
      print("The parking lot is full.Please wait for sometime.Sorry for the inconvineince!!!")
      break   
    if "Park" in l[i] :
        if "" in ci:
            idx = ci.index("")
            ci[idx] = l[i][5:18]
            di[idx] = int(l[i][-2:])
        else:
            ci.append(l[i][5:18])
            di.append(int(l[i][-2:]))

        print("Car with vehicle registration number " + '"' + str(l[i][5:18]) +'"' + " has been parked at slot number " +
              str(ci.index(l[i][5:18]) + 1))
        #print(ci,di)
        #print(di)
    if "Slot" in l[i]:
        if "driver" in l[i]:
            d = int(l[i][-2:])
            dl = []
            for i in range(len(di)):
                if di[i] == d:
                    dl.append(i + 1)
            print(",".join(str(i) for i in dl))

        else:
            c = "".join(l[i][-13:])
            print(ci.index(c) + 1)
    if "Leave" in l[i]:
        print("Slot number " + str(l[i][-1]) + " vacated, the car with vehicle registration number " + '"' +ci[int(l[i][-1]) - 1] + '"' +" left the space, the driver of the car was of age " +str(di[int(l[i][-1]) - 1]))
        ci[int(l[i][-1]) - 1] = ""
        di[int(l[i][-1]) - 1] = 0
