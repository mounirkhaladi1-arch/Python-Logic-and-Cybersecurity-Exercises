#!/usr/bin/env python3

#To print a reversed string, we print the characters in reverse order.
# We use the index [::-1], where the negative sign indicates reading from right to left.
# We use the slice [::-1]. It works on the logic of [start:stop:step].
# By leaving the first two indices empty, it tells Python to automatically span the entire string.
# Because the step is negative, Python automatically starts at the last character and ends at the first.

print( 'rekcah_repus'[::-1])