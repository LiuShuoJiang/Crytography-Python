val = (4 + 15) % 12
print(val)

val = (4 * 5) % 12
print(val)

# Generators
g = 2
for i in range(10):
    print(i, (g**i) % 5)
