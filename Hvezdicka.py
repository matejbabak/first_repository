def printstars(cislo):
    for i in range(cislo):
        print(cislo*"*")

print(printstars(5))


def printstars_triangle(cislo):
    for i in range(cislo):
        print((cislo-i)*"*")
        
print(printstars_triangle(5))


def printstars_triangle_2(cislo):
    count_stars = 2
    space_count = (cislo//2) - 1
    while count_stars < (cislo):
        print(space_count*" " + count_stars*"*")
        count_stars += 2
        space_count += -1

print(printstars_triangle_2(5))

def printstars_triangle_3(cislo):
    count_stars_3 = 1
    space_count_3 = (cislo*2 - 1)//2
    while count_stars_3 <= (cislo*2 - 1):
        print(space_count_3*" "+count_stars_3*"*")
        count_stars_3 += 2
        space_count_3 -= 1

print(printstars_triangle_3(5))

def printstars_square(cislo):
    count_stars = 2
    space_count = (cislo//2) - 1
    while count_stars < (cislo):
        print(space_count*" " + count_stars*"*")
        count_stars += 2
        space_count += -1
    count_stars_2 = (cislo//2)*2 - 2
    space_count_2 = (cislo - count_stars_2) // 2
    while count_stars_2 > 0:
        print(space_count_2*" " + count_stars_2*"*")
        count_stars_2 -= 2
        space_count_2 += 1

print(printstars_square(5))

def printstars_tree(cislo):
    for i in range(cislo+1):
        count_stars_3 = 1
        space_count_3 = cislo-1
        count = 1
        while count <= i:
            print(space_count_3*" "+count_stars_3*"*")
            count_stars_3 += 2
            space_count_3 -= 1
            count += 1
        
print(printstars_tree(5))
