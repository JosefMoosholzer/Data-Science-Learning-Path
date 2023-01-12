from time import perf_counter
tic1 = perf_counter()
even_pairs = [(x,y) for x in range(10000) if x%2==0 for y in range(10000) if y%2==0]
#print(even_pairs)
toc1 = perf_counter()
print(toc1-tic1)
tic2 = perf_counter()
even_pairs = [(x,y) for x in range(10000) for y in range(10000) if x%2==0 and y%2==0]
#print(even_pairs)
toc2 = perf_counter()
print(toc2-tic2)
