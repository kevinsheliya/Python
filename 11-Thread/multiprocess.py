import multiprocessing
import time

def sqr_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube : {i*i*i}")


if __name__ == '__main__':

    # process separete
    p1=multiprocessing.Process(target=sqr_num)
    p2=multiprocessing.Process(target=cube_num)

    t=time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    Endtime=time.time()-t
    print("Ending time :",Endtime)
