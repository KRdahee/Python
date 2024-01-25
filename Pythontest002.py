#친구에게 어제 봤던 별자리를 print()를 이용해서 보여줍시다!
"""
for i in range(5):
    print('{:<5}'format('*'*(i+1)))
"""
"""
for i in range(5):
    for j in range(i+1):
        print('*',end="")
        print('')
"""
a = 5
for i in range(a): 
    print('*' * (i+1))

"""
*
**
***
****
*****
"""