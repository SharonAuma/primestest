import math
for num in range(1,101):
        prime=True
        for i in range(2,num/2):
            if (num%i==0):
              prime=False
        if prime:
           print num