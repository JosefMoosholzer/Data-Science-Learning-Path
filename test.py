from time import perf_counter


# Generator with comprehension


# Generator with yield
for _ in range(5):
    tic = perf_counter()
    def generator_odd_pairs(n):
        x,y = 0,0
        while x < n:
            while y < n:
                yield x,y
                y += 2
            x += 2

    for x,y in generator_odd_pairs(10000):
        sum_of_both = x+y
    toc = perf_counter()
    print(toc-tic) # Consistently less than 0.0013 seconds