# Pavitra Behara
# 2041002041

# ____________________________________________________________________________________

# Question 0

# Data Science Project

# users = [
#     { "id": 0, "name": "Hero" },
#     { "id": 1, "name": "Dunn" },
#     { "id": 2, "name": "Sue" },
#     { "id": 3, "name": "Chi" },
#     { "id": 4, "name": "Thor" },
#     { "id": 5, "name": "Clive" },
#     { "id": 6, "name": "Hicks" },
#     { "id": 7, "name": "Devin" },
#     { "id": 8, "name": "Kate" },
#     { "id": 9, "name": "Klein" },

# ]
# friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# 1.	Creation of DataSciencester Network
# 2.	Find the total number of connections and average connections of the network
# 3.	Sort from “most friends” to “least friends”
# 4.	Find the friends of friends

# ___________________________________________________________________________________


# Code _______________________________________________________________________________

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                    (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# OBJECTIVE - 1 : Creation of DataSciencester Network

# Creating array for each id which is nothing but friend list
relation = {}
for e in users:
    relation[e['id']] = []

# making friendship connection
for i, j in friendship_pairs:
    relation[i].append(j)
    relation[j].append(i)

print(relation)

# OBJECTIVE - 2 : Find the total number of connections and average connections of the network

# this function counts no of friends for each user


def total_friends(user):
    friend_count = relation[user['id']]
    return len(friend_count)


# sum for total connections
sum = 0

for e in users:
    total = total_friends(e)
    sum += total
    print(f"ID:{e['id']}, Total Friends : {total}")

print(f'Total no of connections are {sum}')
print(f'Average connections {sum/len(users)}')

# OBJECTIVE - 3 : Sort from “most friends” to “least friends”

temp = []

for e in users:
    temp.append((e['id'], total_friends(e)))
temp.sort(key=lambda x: x[1], reverse=True)
print(temp)

# OBJECTIVE - 4 : Find the friends of friends
index = int(input('Enter id to check friends of friends : '))

fr = relation[index]
print(f'id:{index}, Friends:{fr}')

for e in fr:
    print(f'id:{e}, Friends:{relation[e]}')
