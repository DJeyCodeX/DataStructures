
def pair_sum(a,b):
    print(a+b)


def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total


pair_sum_sequence(4) ##try to debug, will find that every time it runs it will remove previous call from the memory.