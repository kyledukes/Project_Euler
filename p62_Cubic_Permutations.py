"""
Cubic permutations
Problem 62 

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). 

In fact, 41063625 is the smallest cube which has exactly three permutations 
of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

def count_permutations(cube_sort, cube, counts):
    if cube_sort in set(counts.keys()):
        counts[cube_sort].append(cube)
        return len(counts[cube_sort])
    else:
        counts[cube_sort] = [cube]
        
def find_smallest_cube(amount_of_permutations):
    lens_sorts = {}
    counts = {}
    n = 0
    while True:
        n += 1
        cube = n ** 3
        cube_s = str(cube)
        cube_sort = "".join(sorted(cube_s))
        if len(cube_sort) in set(lens_sorts.keys()):
            if cube_sort in set(lens_sorts[len(cube_sort)]):
                if count_permutations(cube_sort, cube, counts) == amount_of_permutations:
                    return counts[cube_sort][0]
            else:
                lens_sorts[len(cube_sort)].append(cube_sort)
                count_permutations(cube_sort, cube, counts)
        else:
            lens_sorts[len(cube_sort)] = [cube_sort]
            
print(find_smallest_cube(5))