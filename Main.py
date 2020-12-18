# add = 0
# for i in range (0,20,3) :
#     print("Multiples of 3:", i)
#     add = add + i;
# print("Sum of multiples of 3:", add)
#
# for j in range (0,20,5) :
#     print("Multiples of 5:", j)
#     add = add + j;
# print("Sum of multiples of 3 and 5:", add)

count = 0
add = 0
for count in range(1000):
    if count % 3 == 0:
        print(count)
        add = add + count;

    elif count % 5 == 0:
        print(count)
        add = add + count;

    elif (count % 3 == 0 and count % 5 == 0):
        continue

print("Sum of multiples of 3 and 5:", add)