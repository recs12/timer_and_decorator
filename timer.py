from datetime import datetime
import time
from delorean import Delorean

# try decorator for timing stuff
# print(datetime.now())


d = Delorean()
d = d.shift('US/Eastern')
print(d.datetime)
print(d.date)
# print(naive)
print()


# tic = time.perf_counter()
# for i in range(100):
#     print(i)
# toc = time.perf_counter()
# diff = toc - tic
# print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")