import time
start = time.time()

def float_add():
  a = 1.0
  b = 2.0
  for i in range(100000):
    for j in range(100000):
      c = a + b
      
float_add()