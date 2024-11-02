import time 
import threading
import concurrent.futures

# multithreading vs multiprocessing
'''
start = time.perf_counter()
def do_multithread(sec):
    print('sleeping for 1 sec...')
    time.sleep(sec)
    print('Done sleeping ')


# t1 = threading.Thread(target=do_multithread)
# t2 = threading.Thread(target=do_multithread)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads =[]
for _ in range(10):
    t = threading.Thread(target=do_multithread,args=[1.5])
    t.start()
    threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print('Finished in {} seconds'.format(finish - start))
'''

start = time.perf_counter()
def do_multithread(sec):
    print('sleeping for 1 sec...')
    time.sleep(sec)
    return 'Done sleeping '

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_multithread,1)
    f2 = executor.submit(do_multithread,1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print('Finished in {} seconds'.format(finish - start))