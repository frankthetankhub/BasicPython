#1.1
import numpy as np

s1 = "the quick brown fox jumps over the lazy dog"
s2 = " the quick \n brown fox jumps over the lazy dog"
s3 = "the\t\t\tquickbrownfoxjumpsoverthe lazy dog"
def _split(s):
    ls = s.split()
    s = ""
    for w in ls:
        s += w
    return s

s4 = _split(s1)
s5 = _split(s2)
s6 = _split(s3)
print(s4)
print(s5)
print(s6)
print()

#1.2
list_of_numbers = [4.3,6,9.2,1.77029,42]
avg = np.mean(list_of_numbers)
print("{:.5f}".format(avg))
