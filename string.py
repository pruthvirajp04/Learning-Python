#B-11 Pruthviraj Patil
string  = 'pruthviraj'
print (string)
print("First char :",string[0] )
print("Last three char :", string[7:10])
string = string.capitalize()
print (string)   #Capitalises first letter
print(string.upper())    #Upper case
print(string.lower())  #Lower case
print(string.find("raj"))    #returns the index from where "raj" was starting
print(string.center(20))
string = "Pruthvi{lname:}"
print(string.format(lname = "raj")) #formats string accordingly