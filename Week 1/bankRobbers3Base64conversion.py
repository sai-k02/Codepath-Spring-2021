#Developer: Srilokh Karuturi
# Code Path Cyber Security Lab Bank Robbers 3
# Purpose:
# Take the numbers -100 to 100 and convert via base 64 and reverse


#package for using base 64
import base64


#function to reverse strings 
def my_function(x):
  return x [::-1]
  
# list containing starting values
numbers = []
numbers.extend(range(-100,101))

#base 64 conversion list
b_numbers = []

#final REVERSE base 64 list
f_numbers = []



#For loop for converting the numbers into base 64

for x in numbers:
    x_bytes = str(x).encode("ascii")
    base64_bytes = base64.b64encode(x_bytes)
    base64ascii = base64_bytes.decode("ascii")
    reverse = my_function(base64ascii)
    b_numbers.append(reverse)
    
    
# for loop for stripping away ==
for x in b_numbers:
    final = x.strip('==')
    f_numbers.append(final)
    

# printing to console and removing the '' around the list elements.
    
print('[' + ', '.join(f_numbers) + ']')



