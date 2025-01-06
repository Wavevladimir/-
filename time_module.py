import time
print(time)
start_time  = time.time()
print(time.ctime(2345463245))

time.sleep(2.5)
end_time = time.time()
print(start_time - end_time)

import time

startt_time = time.time()

my_range = range(1000000)
print(my_range[1000])

endd_time = time.time()

print("Total duration of the operation: ", endd_time - startt_time)