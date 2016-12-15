# 测试dict函数是否copy 
addr = {'Hellen':'1234','Angel':'4567'}
addr2 = dict(addr)
addr['Angel'] = '5678'
print (addr)
print (addr2)

# 测试字典的使用
people = {
    'Alice':{
        'phone': '2341',
        'addr' : 'Foo drive 23'
        },
    'Beth': {
        'phone': '9102',
        'addr' : 'Bar street 42'
        },
    'Cecil': {
        'phone': '3178',
        'addr' : 'Baz avenue 90'
        }
    }

labels = {'phone': 'phone number',
          'addr': 'address'
          }
# define the name variable
name = input('Name;')
request = input("Phone number (p) or address (a)?")
                
if request == 'p' : key = "phone"
if request == 'a' : key = "addr"
print (key)

if name in people: print ("%s's %s is %s." % \
                         (name, labels[key], people[name][key]) )

print ("All the information for Alice is " + "%(Alice)s" % people )
