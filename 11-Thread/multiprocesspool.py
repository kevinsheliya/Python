from concurrent.futures import ProcessPoolExecutor
import time


def print_suq(numbers):
    time.sleep(2)
    return f"SQUARE NO : {numbers}"

numbers=[1,2,3,4,5,6,7,8,9,0]

if __name__ == '__main__':
    t=time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(print_suq,numbers)

    for result in results:
        print(result) 

    print("End time :",time.time()-t )
