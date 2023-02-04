import time

start = time.time()
def int_add():
  a = 1
  b = 2
  for i in range(100000):
    for j in range(100000):
      c = a + b
      
int_add()

def int_mult():
  a = 1
  b = 2
  for i in range(500000):
    for j in range(10000):
      c = a*b
int_mult()


    
