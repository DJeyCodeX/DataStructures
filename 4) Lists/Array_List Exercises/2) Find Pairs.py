# Write a program to find all pairs of integers whose sum is equal to a given number.

# Example [2,6,3,9,11] , 9 --> [6,3]

#Valid Questions for this problem
# -  Does array contain only positive or negative numbers.
# - What if the same pair repeats twice, should we repeat it every time?
# - if the reverse of the pair is acceptable, ex- can we print both 4,1 and 1,4 if the given them sum is five?
# - do we need to print only distinct pairs? Does 3,3 is a valid pair for given sum of six.
# - how big the array is?

# Now here we are going to develop our method. Now here before starting to develop our method,
# I want to mention that the pairs has to be distinct, which means that 2,2 or 3,3 is not a valid pair.

def find_pairs(arr, target_sum):
    seen = set()
    output = []

    for num in arr:
        print("seen", seen)
        print("output", output)
        complement = target_sum - num
        print("Complement", complement)
        print("num", num)
        if complement in seen:
            output.append((complement, num))
        seen.add(num)
        print("seen after append", seen)
        print("output after append", output)
        print("-----------------------")

    return output


print(find_pairs([2,6,3,9,11], 9))