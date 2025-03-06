# squares=[x**2 for x in range(10)]
# print(squares)

# even_squers=[x**2 for x in range(1,11) if x % 2==0]
# print(even_squers)

# odd_squers=[x**2 for x in range(1,11) if x % 2==1]
# print(odd_squers)

# pairs=[(x,x**2) for x in range(1,5)]
# print(pairs)

# matrix=[[1,2,3,4],[5,4,2],[6,7,8,9]]
# flatten=[element for row in matrix for element in row ]
# print(flatten)

# --------------> printing prime numbers
def is_prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

primes=[x for x in range (2,51) if is_prime(x)]
# print(primes)

prices=[120,55,200,143,90]
disc_prices=[price*0.8 if price>100 else price for price in prices]
print(disc_prices)

# You have a list of strings, and you want to extract all digits from these strings and
# combine them into a single list.
strings = [
"abc123",
"hello456world",
"789",
"test"
]

ans=[char for row in strings for char in row ]
print(ans)

dig=[]
for row in strings:
    for char in row:
        if char.isdigit():
            dig.append(int(char))
print(dig) 