import threading

def factorial_partial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def parallel_factorial(n, num_threads=4):
    
    chunk_size = n // num_threads

    
    threads = []
    results = [None] * num_threads
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size if i < num_threads - 1 else n
        t = threading.Thread(target=lambda idx, s, e: results.__setitem__(idx, factorial_partial(s, e)), args=(i, start, end))
        t.start()
        threads.append(t)

   
    for t in threads:
        t.join()

  
    final_result = 1
    for res in results:
        final_result *= res

    return final_result


number, num_thread = map(int, input().split())
print(parallel_factorial(number, num_thread))
