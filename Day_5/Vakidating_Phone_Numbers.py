import re
for i in range(int(input())):
    Ph = input()
    if re.match(r'[789]\d{9}$',Ph):
        print ('YES')
    else:
        print ('NO')  
