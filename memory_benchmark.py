import time

start = time.time()
nums = []
def write_array():
  global nums
  for i in range(100):
    nums = [i for i in range(5000000000//100)]

write_array()
  
