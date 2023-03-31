def smgenerator(ordinates):
    sm = []
    if (len(ordinates)-1) %2 == 0:
        r = int((len(ordinates)-1)/2)
        for i in range(r):
                sm.append([1, 4, 1])

    
    elif (len(ordinates)-1) %3 == 0:
        r = int((len(ordinates)-1)/3)
        for i in range(r):
            sm.append([1,3,3,1])

    else:
         ordinates = ordinates[0:-2]
         sm = smgenerator(ordinates)
         sm.append([1, 4, 1])

    index = {}
    ix = 1
    for i, ele in enumerate(sm):
         ix -= 1
         for j in ele:
              index[ix] = i
              ix += 1

    for i, ele in enumerate(ordinates):
         if ele == 0 or i == (len(ordinates)-1):
              continue
         pos = index[i]
         if ele<1 or ele % int(ele) != 0:
              if ordinates[i+1] % int(ordinates[i+1]):                  
                   if len(sm[pos]) == 4:
                        sm[pos] = [0.5, 1.5, 1.5, 0.5]
                   else:
                        sm[pos] = [0.5, 2, 0.5]
                        for j in range(pos+1,len(sm)):
                             if len(sm[j]) == 4:
                                  sm.pop(j)
                                  sm.append([1,3,3,1])
                                  break
                             #TODO: else, change combination
              else:
                   if len(sm[pos]) == 3:
                        sm[pos] = [0.5, 2, 0.5]
                   else:
                        sm[pos] = [0.5, 1.5, 1.5, 0.5]
                        for j in range(len(sm)):
                             if j == pos:
                                break
                             if len(sm[j]) == 3:
                                  sm.pop(j)
                                  sm.append([1,4,1]) 
                                  break
                             #TODO: else, change combination               
                                         
    return sm


# ordinates = [0, 0.5,  1, 1.5,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18.5, 19, 19.5, 20]

# print(smgenerator(ordinates))
# print(len(ordinates))

