arrayv = []
arrayh = []
dicth = {}
dictv = {}
def sol():

    f = open('a_example.txt','r')
    N = int(f.readline())
    #arraymapper
    for line in range(N):
        linecontent = f.readline().split()
        if (linecontent[0] == "H"):
            for i in range(int(linecontent[1])):
                if linecontent[i + 2] not in arrayh:
                    arrayh.append(linecontent[i + 2])
        elif (linecontent[0] == "V"):
            for i in range(int(linecontent[1])):
                if linecontent[i + 2] not in arrayv:
                    arrayv.append(linecontent[i + 2])

    print(len(arrayh))
    print(len(arrayv))
    arrayh.sort()
    arrayh.sort()
    #dictionary maker
    temp = []
    f.close()
    z= open('c_memorable_moments.txt','r')
    for photo in range(N):
        photos = z.readline().split()
        if (photos[0] == 'H'):
            for tag in arrayh:
                if tag not in photos:
                    temp.append(0)
                else:
                    temp.append(1)
            dicth[photo] = temp
        if (photos[0] == "V"):
            for tag in arrayv:
                if tag not in photos:
                    temp.append(0)
                else:
                    temp.append(1)
            dictv.update({photo : temp})

    print(dictv)

sol()


    # print("horizontal = %d and vertical = %d " % (horizontal,vertical))
