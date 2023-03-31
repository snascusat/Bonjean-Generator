
def generateTable():
    print("Hey there, welcome to hydrostatics table generator :)"
          "Give us your vessel particulars and we're all set to begin!"
          "\n")

    length = float(input("Design length of the vessel: "))
    breadth = float(input("Design beam of the vessel: "))
    depth = float(input("Depth of the vessel: "))

    stations = int(input("Number of stations in the design: "))
    waterlines = int(input("Enter the number of waterlines: "))

    stnList = list(range(stations+1))
    stnSpacing = length/stations

    print("So, your station spacing must be ",stnSpacing, "\n"
          "and the stations must be ", stnList,
          "\nYou want to add some intermediate stations? (y/n) "  )
    ans = input()
    if ans== 'y':
        n = int(input("Enter number of intermediate stations : "))

        for i in range(0, n):
            ele = float(input("Enter: "))
            stnList.append(ele)
            stnList.sort()

        print("New stations are ",stnList)

    wtlList = list(range(waterlines+1))
    wtlSpacing = depth/waterlines

    print("\nYour waterline spacing must be ",wtlSpacing, "\n"
          "and the waterlines must be ", wtlList,
          "\nYou want to add some intermediate waterlines? (y/n) "  )
    ans = input()
    if ans== 'y':
        n = int(input("Enter number of intermediate waterlines : "))

        for i in range(0, n):
            ele = float(input("Enter: "))
            wtlList.append(ele)
            wtlList.sort()

        print("New waterlines are ",wtlList)

    print("Now, let's input the half-breadths for each waterlines and stations.")
    offsetTable =[]

    for waterline in wtlList:
        halfBreadth = []
        print("WATERLINE : ", waterline)
        for station in stnList:
            halfBreadth.append(float(input("Station "+str(station)+":")))
        offsetTable.append(halfBreadth)

    print("The Table of Offsets:"
          "\n",offsetTable)










if __name__ == '__main__':
    generateTable()


