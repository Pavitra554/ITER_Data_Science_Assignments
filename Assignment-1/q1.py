# Pavitra Behara
# 2041002041

# ____________________________________________________________________________________

# Question 1

# An anonymous dataset containing each user’s salary (in dollars) and tenure as a data scientist (in
# years) is given.
# salaries and tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7),
# (76000, 6), (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
# (48000, 1.9), (63000, 4.2)]
# Find out the average salary for each tenure and print a massage according to its value, i.e. ”less than
# two”, ”between two and five” and ”more than five” tenure and group together the salaries corresponding to each bucket. Compute the average salary for each group.

# ___________________________________________________________________________________


# Code _______________________________________________________________________________

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (
    69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]

# Defining the groups
g1 = []  # Less Than Two
g2 = []  # Between two and five
g3 = []  # More than five

# Filtering elements in groups
for s, t in salaries_and_tenures:
    if t < 2:
        print(f'({s},{t}) --> Less Than Two')
        g1.append(s)
    elif t >= 2 and t <= 5:
        print(f'({s},{t}) --> Between Two and five')
        g2.append(s)
    else:
        print(f'({s},{t}) --> More sthan five')
        g3.append(s)

print("Average salary for less than two years of tenure:",
      sum(g1)/len(g1))
print("Average salary for two to five years of tenure:",
      sum(g2)/len(g2))
print("Average salary for more than five years of tenure:",
      sum(g3)/len(g3))
