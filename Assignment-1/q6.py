# Pavitra Behara
# 2041002041

# ___________________________________________________________________________________

# Question 6
# Read a lists named StringList1 containing strings from the key board. Generate a string MStringList1
# that contains all items of StringList1 that are repeated twice or more number of times and print this
# list. By observing the outcome of MStringList1 perform the following tasks:
#   a. Check wather an item of MStringList1 occurs even number of times or odd number of times in StringList1.
#   b. Remove the ith (i ≥ 2) occurrence of a given word in a StringList1.

# ____________________________________________________________________________________


# Code _______________________________________________________________________________


StringList1 = input('Enter List of Strings : ').split()

MStringList1 = []

for e in StringList1:
    if StringList1.count(e) >= 2:
        MStringList1.append(e)

for item in MStringList1:
    if StringList1.count(item) % 2 == 0:
        print(item, "occurs an even number of times in StringList1")
    else:
        print(item, "occurs an odd number of times in StringList1")


word = input('Enter word for removing...')
count = 0
for i in range(len(StringList1)):
    if StringList1[i] == word:
        count += 1
        if count >= 2:
            del StringList1[i]
            break

print("Modified StringList1:", StringList1)
