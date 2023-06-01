"""
    Name: Two Sets of Equal Sum
    Rank: 6kyu
    Prompt: Task
If possible, divide the integers 1,2,…,n into two sets of equal sum.

Input
A positive integer n <= 1,000,000.

Output
If it's not possible, return [ ] (Javascript and Python) or ( ) (Python) or None (Scala). If it's possible, return two disjoint sets. Each integer from 1 to n must be in one of them. The integers in the first set must sum up to the same value as the integers in the second set. The sets can be returned in a tuple, list, or array, depending on language.
"""
# Solution

def create_two_sets_of_equal_sum(n): ## Divide the numbers 1,2,…,n into two sets of equal sum.
    if n % 4 == 0 or (n + 1) % 4 == 0:
        sequence = range(1, n + 1)
        total = sum(sequence) / 2
        set1 = [*sequence]
        set2 = []
        while total > 0:
            if set1[-1] < total:
                num = set1.pop()
                set2.append(num)
                total -= num
            else:
                set2.append(total)
                set1.remove(total)
                total = 0
        print(n, ": ", set1, set2)
        return (set1, set2)
    else:
        print(n, ": No solution")
        return []

# Notes: 
# The * in "set1 = [*sequence]" unpacks the range into its commposite values
# I wanted to use set2.insert(1, (number)) rather than set2.append, but that timed out the tests; the cost of insert
#   might be kind of high. Sum also takes a toll, and few of the solutions I saw used it; it appears a formula for the sum of 
#   n integers is something like (n * (n +1) / 2). 
# A lot of the solutions used range in clever ways to compose their solution sets.
# It's a small thing, but rather than use "if n % 4 == 0 or (n + 1) % 4 == 0", a lot of solutions used something like 
#   "if n % 4 in (0, 3)", which saves some typing
# Also, one of the numbers in the range seemingly is or gets converted to a decimal value for some reason? The math still works,
#   but I don't know where that's coming from. In general, I could stand to get some more practice with range   

"""
The basic setup: two sets of equal sum means that the sum of numbers 1, 2, ..., n needs to be
an even number. This happens when:
    the sum of numbers 1, 2, ..., n - 1 is odd, and n is an odd number, or
    the sum of numbers 1, 2, ..., n - 1 is even, and n is an even number
This happens in an alternating pattern:
    n = 3: total is 6, [1, 2], [3]
    n = 4: total is 10, [1, 4], [2, 3]
    n = 5: total is 15
    n = 6: total is 21
    n = 7: total is 28, [3, 4, 7], [1, 2, 5, 6]
    n = 8: total is 36, [3, 7, 8], [1, 2, 4, 5, 6]
    n = 9: total is 45
    n = 10: total is 55
    n = 11: total is 66, [5, 8, 9, 11], [1, 2, 3, 4, 6, 7, 10]
    and so on. 
Rather than manually summing the numbers, we should be able to determine if a solution exists by
    testing if n or (n + 1) is divisible by 4
The real problem is how to create a solution set; we basically just need to make an array of 
    integers 1, 2, ..., n, remove numbers from that array that add up to the sum of the range / 2,
    store them in a new array, and then return the two arrays, but picking numbers until it 
    matches the target value is an interesting question. After n = 4, there are multiple possible
    solutions. The quickest method for generating solution that I can think of is maximizing the 
    values in one set by starting at n, attempting to add the next lowest values (n - 1, n - 2, 
    and so on) until that would exceed the sum / 2, then adding whatever integer is needed to reach
    that threshold.
"""