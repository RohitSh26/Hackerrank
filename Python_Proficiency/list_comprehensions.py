

# input x, y, z - cuboid dimention
# input n

# problem
# print list of all possible coordinates given by (i, j, k) on a 3D grid
# where sum(i + j + j) != n

# constraints
# 0 <= i <= x;  0 <= j <= y;  0 <= k <= z

# check how input will look like
# if x = 1, i = 0 and 1


def get_list_comprehesions(x, y, z, n):
    arr = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z +1) if( i + j + k) != n]
    print(arr)




if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

    x = 1
    y = 1
    z = 1
    n = 2

    get_list_comprehesions(x, y, z, n)




