#### 1. Numeric
# 1. int 
#int var  #variable declaration
var=10    #variable initialization
print(type(var))

# 2. float
var = 3.14
print(type(var))

# 3. complex
var=10+5j    #real & imaginary
print(type(var))

##### 2. Text
# 1. str
var='first "bit" solution'
var="firstbit's solutions"
var='''this is first line.
this is next line.
;lksdjf1;kj'''
var="this is first line. this is next line."
print(type(var))
print(type(var))
print(type(var))
print(type(var))

#### 3 . Sequential
# 1. list
var=[10,20,30,40]
print(type(var))

# 2. tuple
var=(10,20,30,40)
print(type(var))

# 3. range
var=range(1,11)
print(type(var)) 

#### 4. Set type
# 1. set
var={10,20,30}
print(type(var))

# 2. frozenset
var=frozenset({10,20,30})
print(type(var))

#### 5.Mapping
# 1. dict
var={'id':101, 'name':'XYZ'}
print(type(var))

#### 6. Others
# 1. Boolean
var=True
var=False
print(type(var))
print(type(var))

# 2. none
var=None
print(var)
print(type(var))