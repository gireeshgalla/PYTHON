'''
list
'''

'''
v=[]
print((type(v)))
'''
'''
v=[1,24,1,4,1544,5,'kiran']
print(v[v])
'''

''' 
v=[1,24,1,4,1544,5,'kiran']
print(v[-1])
'''

'''
v=[1,24,1,4,1544,5,'kiran']      #Slice
print(v[0:4:2])
'''


'''
Append
Extend
Count
Insert
pop
Remove
Index
'''

'''
v=[1,24,1,4,1544,5,'kiran']     #To add the element at last is called Append
v.append("python")
print(v)
'''

'''
V=[1,24,1,4,1544,5,'kiran']
V.extend([5,36,36,46346])       #To add Bulk Data(List of Data) is called Extend
print(V)
'''


'''
v=[1,24,1,4,1544,5,'kiran']
print(v.count(1))                #Count
'''

''''
v=[1,24,1,4,1544,5,'kiran']
v.remove(1)                       #Remove
print(v)
'''


'''
v=[1,24,1,4,1544,5,'kiran']
v.pop(1)                            #pop
print(v)
'''


'''
v=[1,24,1,4,1544,5,'kiran']
print(v.index(24))                  #Index
'''



v=[1,24,1,4,1544,5,'kiran']
v.insert(0,"xyz")                    #Insert
print(v)