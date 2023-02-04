import time

start = time.time()
def write_file():
  with open('file.txt', 'wb') as f:
    for i in range(100):
      for j in range(1000):
        f.write(b'\xAB'*10000)
        
write_file()
