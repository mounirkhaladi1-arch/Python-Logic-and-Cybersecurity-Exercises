#!/usr/bin/env python3



# printing by performing a for loop

for i in range(1,101):      # Note:the range will stoop at 100 not 101
    if i%4 != 0 :       # Checking that the numbers that would be printed  are not  divisible by 4
        print(i)
    else:
        continue
