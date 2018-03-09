# recursion needs 2 things:
# 1.) base case (ex in factorials, base case is 1)
# 2.) recursive step (ex in factorials, recursive step is 1 because change by 1 each time)
# always establish whats your base base and whats your recursive step

# recursive actually bad way to do this. REcursvie can be terrible for opt and memory leaks

def recur_factorial(num):
    if num == 1:
        return num
    else:
        print(num * recur_factorial(num - 1))
        return num * recur_factorial(num - 1)

print(recur_factorial(3))


def iter_factorial(num):
    counter = num
    
