

import numpy as np

# Number of users in our example
users = ["Alice", "Bob", "Charlie", "David", "Esha"]

# Create an empty adjacency matrix
n = len(users)
adjacency_matrix = np.zeros((n, n), dtype=int)

# Add friendship connections
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "David"),
    ("Charlie", "Esha"),
    ("David", "Esha")
]

# Fill the adjacency matrix
for user1, user2 in friendships:
    i = users.index(user1)
    j = users.index(user2)

    # Friendship is mutual
    adjacency_matrix[i][j] = 1
    adjacency_matrix[j][i] = 1

# Display the matrix
print("Users:")
print(users)

print("\nSocial Network Adjacency Matrix:")
print(adjacency_matrix)

# Find friends of a particular user
user = "Alice"
index = users.index(user)

friends = []

for i in range(n):
    if adjacency_matrix[index][i] == 1:
        friends.append(users[i])

print(f"\nFriends of {user}:")
print(friends)