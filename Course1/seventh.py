# from threading import Thread
# import time


# def grow_plants(duration):
#     time.sleep(duration)
#     print("The plants are grown!")


# def listen_to_music(duration):
#     time.sleep(duration)
#     print("The music is played!")


# def cook_meal(duration):
#     time.sleep(duration)
#     print("The meal is cooked!")


# def run_sequential(durations):
#     start_time = time.time()

#     # TODO: برنامه را طوری تکمیل کنید که توابع بالا به‌طور متوالی اجرا شوند.
#     grow_plants(durations[0])
#     listen_to_music(durations[1])
#     cook_meal(durations[2])


#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(f"Sequential execution time: {elapsed_time:.1f} seconds")


# def run_threaded(durations):
#     start_time = time.time()

#     # TODO: برنامه را طوری تکمیل کنید که زمان اجرا کمتر شود.

#     th1 = Thread(target=grow_plants,args=(durations[0],))
#     th2 = Thread(target=listen_to_music,args=(durations[1],))
#     th3 = Thread(target=cook_meal,args=(durations[2],))

#     th1.start()
#     th2.start()
#     th3.start()

#     th1.join()
#     th2.join()
#     th3.join()

#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(f"Threaded execution time: {elapsed_time:.1f} seconds")


# durations = list(map(float, input().split()))
# run_sequential(durations)
# run_threaded(durations)


# # IMPORTS
# import functions
# from threading import Thread

# def threadize() -> None:
#     f_threads = [Thread(target=functions.f[i], name=(i + 1)) for i in range(len(functions.f))]

#     for thread in f_threads :
#         thread.start()
#     for thread in f_threads :
#         thread.join()

#     g_threads = [Thread(target=functions.g[i], name=(i + 1)) for i in range(len(functions.g))]

#     for thread in g_threads :
#         thread.start()
#     for thread in g_threads :
#         thread.join()

#     h_threads = [Thread(target=functions.h[i], name=(i + 1)) for i in range(len(functions.h))]

#     for thread in h_threads :
#         thread.start()
#     for thread in h_threads :
#         thread.join()


from threading import Thread, Lock

lock = Lock()

def synchronized(func):
    def inner_function( *args , **kwargs ) :
        lock.acquire()
        func( *args , **kwargs )
        lock.release()
    return inner_function


a = 0

@synchronized
def f():
    global a
    for i in range(300000):
        a += 1

t = Thread(target=f)
s = Thread(target=f)

print("Starting threads...")

t.start()
s.start()

t.join()
s.join()

print("Threads finished.")

print(f'{a = }')