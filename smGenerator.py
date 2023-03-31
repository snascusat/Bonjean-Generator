def smgenerator(stn):
    sm = []
    if (len(stn)-1) %2 == 0:
        r = int((len(stn)-1)/2)
        for i in range(r):
                sm.append([1, 4, 1])

    
    elif (len(stn)-1) %3 == 0:
        r = int((len(stn)-1)/3)
        for i in range(r):
            sm.append([1,3,3,1])

    else:
         stn = stn[0:-2]
         sm = smgenerator(stn)
         sm.append([1, 4, 1])

    index = {}
    ix = 1
    for i, ele in enumerate(sm):
         ix -= 1
         for j in ele:
              index[ix] = i
              ix += 1

    for i, ele in enumerate(stn):
         if ele == 0 or i == (len(stn)-1):
              continue
         pos = index[i]
         if ele<1 or ele % int(ele) != 0:
              if stn[i+1] % int(stn[i+1]):                  
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


stn = [0, 0.5,  1, 1.5,  2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18.5, 19, 19.5, 20]

print(smgenerator(stn))
print(len(stn))

