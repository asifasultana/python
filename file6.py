#string data type
x = """well ordered 
by 




saleem"""
print(x)

y = "well ordered \n\n\n\nby junaid \nsaleem"
print(y)

# string is an array
x = "python program"
print(x[-1],x[13])
print(len(x))
  
  
#in and notin
  
z = "junaid" not in x #notin
print(z)

a = "python" in x
print(a)


#slicing

x = "i love pakistan"
print(x[4:6])
print(x[9:3])

print(x[-4:])

print(x[:-4])

# string concatenation
s1 = "great"
s2 = "pakistan"
s3 = s1+s2
print(s3)
s4 = s1 +" "+ s2 
print(s4)
print("hello" + " world")
print(s2*5)

# string format

item = "apple"
qty = 2
price = 30.5
s1 = "i want {} kg {} for {} dollers"
print(s1.format(qty,item,price))

s1 = "i want {0} kg {2} for {1} dollers"
print(s1.format(qty,item,price))
#escaping
a1 = "pakistan is a great country"
print(a1)
a1 = "pakistan is a \"great\"  country"
print(a1)
a1 = "pakistan is a \n \"great\"  country"
print(a1)
a1 = "pakistan is a \\n \"great\"  country"
print(a1)
a1 = "pakistan is a \t \"great\"  country"
print(a1)
a1 = "pakistan is a \\t \"great\"  country"
print(a1)

# string methods

# https://www.w3schools.com/python/python_ref_string.asp

























