from timeit import timeit
from task_22_4 import list_1
from task_24_4 import max_berry

print(timeit("list_1", globals=globals(), number=10))
print(timeit("max_berry", globals=globals(), number=10))
