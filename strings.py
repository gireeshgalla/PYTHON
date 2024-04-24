'''
COllection of characters
'''
#a='pythonlife'
#b="pythonlife"
#c='''pythonlife'''
#print(type(a),type(b),type(c))


'''
lower
upper
endswith
startswith
replace
find
index
count
remove prefix
rem0ve suffix
split
strip
rstrip
lstrip
'''



'''
pythonlife="please subscribe"
print(pythonlife.upper())         #Upper


pythonlife="please subscribe"
print(pythonlife.lower())           #Lower

'''



'''
pythonlife="python language"
print(pythonlife.endswith("language"))     #Endswith----True

pythonlife="python language"
print(pythonlife.endswith("python"))        #Endswith---False
'''


'''
pythonlife="galla gireesh"
print(pythonlife.startswith("galla"))       #Startswith---True

pythonlife="galla gireesh"
print(pythonlife.startswith("gireesh"))      #Startswith---False
'''


'''
pythonlife="galla gireesh"
print(pythonlife.replace("gireesh","eshanth"))   #Replace
'''

''''
pythonlife="galla gireesh"
print(pythonlife.index("galla"))      #0
print(pythonlife.find("galla"))       #0

pythonlife="galla gireesh"
print(pythonlife.index("pandu"))       #Index if we are going to findout the string which is not mentioned in it shows --Error
print(pythonlife.find("pandu"))        #In find if we are going to findout the string which is not mentioned in it shows--_1
'''

'''
pythonlife="galla gireesh"
print(pythonlife.count('e'))            #Count
'''


'''
#pythonlife="galla gireesh"
#print(pythonlife.removeprefix("galla"))
#print(pythonlife.removesuffix("gireesh"))

pythonlife="python language"                      #---?
print(pythonlife.removeprefix("python"))
'''


#pythonlife="python language"
#print(pythonlife.split()
      
pythonlife="     python language     "
print(pythonlife)
print(len(pythonlife))
v=pythonlife.strip()
print(len(v))