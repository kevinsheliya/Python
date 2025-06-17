from concurrent.futures import ThreadPoolExecutor
import time

def print_num(numbers):
    time.sleep(1)
    return f"Number : {numbers}"

numbers=[1,2,3,4,5,6,7,8,9,0]

t=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_num,numbers)


for result in results:
    print(result)

print("End time :",time.time()-t )
