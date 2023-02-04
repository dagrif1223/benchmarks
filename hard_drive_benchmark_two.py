import time

start = time.time()
def write_file():
  with open('file.txt', 'wb') as f:
    for i in range(100):
      for j in range(1000):
        f.write(b'\xAB'*10000)
        
write_file()

def read_file():
  with open('file.txt', 'r') as f:
    for i in range(100):
      for j in range(1000):
        a = f.read(10000)
        
read_file()
end = time.time()
print('The total time in sec for hard drive benchmark 2 was', end-start)
