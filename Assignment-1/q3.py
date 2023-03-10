# Pavitra Behara
# 2041002041

# ___________________________________________________________________________________

# Question 3
# State the difference between the following:
# 1 all() and any()
# 2 str and repr function
# 3 sort and sorted
# 4 random.choice and random.sample

# ____________________________________________________________________________________


# Code _______________________________________________________________________________
import random
# 1
print(all([True, True, False]))
print(any([True, True, False]))

# 2
x = [1, 2, 3]

print(str(x))
print(repr(x))

# 3
x = [3, 1, 2]
x.sort()
print(x)

x = [3, 1, 2]
y = sorted(x)
print(x)
print(y)

# 4
x = [1, 2, 3, 4, 5]
print(random.choice(x))
print(random.sample(x, 3))
