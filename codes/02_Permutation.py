from itertools import permutations
import cProfile

my_list = [1, 2, 3, 4]

list_of_permutations = permutations(my_list)
cnt = 0

for permutation in list_of_permutations:
    print(permutation)
    cnt += 1

print(len(my_list), cnt)
print(type(list_of_permutations))

# print(list(permutations(my_list, 4)))

print('*' * 24)


def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n - 1) * n


def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


for i in range(10):
    print(faculty(i))

cProfile.run("counter(faculty(11))")
