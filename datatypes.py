
"""
datatype tells about the type of data that a variable is holding on 
Datatypes are categorized into "5" types 
1. number
2.sequence
3.boolean
4.set
5.dictionary
"""
#Number--which tells about the number datatypes divided into "3" types
"""
Integer--which holds all the positive and negative whole numbers i.e 0 to n and 0 to -n
Integer can be represented as int()
"""

a=123
print(a)
print(type(a))
print(id(a))
"""
type()-- which tells about the type of a value that internally compiler holding on 
id()-- which tells about the adress location of a  value
"""

a1=-90
print(a1)
print(type(a1)) 
print(id(a1))


"""
float-- which holds the decimal or fractional values i.e 0 to n.n and 0 to -n.n
it can be represented as float()
"""


b=89.456
print(b)
print(type(b))
print(id(b))


b1=-89.456
print(b1)
print(type(b1))
print(id(b1))



"""
complex datatypes are used to hold the real and imaginary values 
which can be represented as a+bj
"""

c=78+67j
print(c)
print(type(c))
print(id(c))

c1=-456+78j
print(c1)
print(type(c1))
print(id(c1)) 


"""
sequence datatypes are divided into"3" types
1.string
2.list
3.tuple
"""

"""
string-- it is a collection / group of chracters
it can be enclosed using the single quotes or double quotes
"""

a="sravsteju"
print(a)
print(type(a))
print(id(a))

d='sravsteju'
print(d)
print(type(d))
print(id(d))


"""
list: it is a collection of items/values/elements
syntax: list name=[val1,val2,..valn]
"""

tejulist = [20, 17.0, 56+17j, 'sravs']
print(tejulist)
print(type(tejulist))
print(id(tejulist))
print(tejulist[2])
print(tejulist[3])
"""
in order to access the elements individually we use indexing
indexing always starts with "0" ends with n-1
syntax to access the elements
print(listname[elemenet position])
"""


"""
tuple is a collection of items /values/elements
syntax= tuplename=(val1,val2,..valn)
"""

mytuple = (12, 12.1, "hi", [1,2,3])
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple[2]) #index(position number)


"""
giving a list with in the list is called sublist
giving a tuple with in a tuple is called subtuple
"""


"""
Boolean : Boolean means check the conddition
they are divided to the two ways
it can be represented as bool
"""

a=True
print(a)
print(type(a))

b=False
print(b)
print(type(b))




"""
set : it is a collection of values/items/elements
syntax : setname{val1, val2,....valn}
a set cant accept the list..
"""

myset={12, 13, 36+56j, "sravsteju",(45, "hello"), True}
print(myset)
print(type(myset))

"""
dictionry : it is a collection of keyvalues pairs
syntax : dictonaryname={key1:val1, key2:val2, ..keyn:valn}
"""


mydict={1:"ists", "branch":"ece yedavalu", 17:"srasv"}
print(mydict)
print(type(mydict))
