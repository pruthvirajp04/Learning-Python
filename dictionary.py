#B-11 Pruthviraj Patil
mydict =	{
  "Name": "Pruthviraj",
  "Branch": "COMPS",
  "DOB": 2002,
    "Div" : 'B',
    "Interest" : "Web"
}
print(mydict)
print(len(mydict)) #Prints length of 'mydict'
fields = ['Students', 'Marks', 'Sports']
values = [20, 85, 5]
dictionary = dict(zip(fields, values))
print(dictionary)   #This is zipping of lists into dict.
mydict.update({"Interest": "App"})
print(mydict)   #Updating into the dict.
print(dictionary.get('Students'))   #Returns the value of field
mydict.pop("Interest")   #Pops 'Interest' field
print(mydict)