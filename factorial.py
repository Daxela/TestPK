import threading
import cachetools

def factorial_1_1(number, number2):
    fact = 1
    for n in range(number, number2+1):
        fact *= n
    global result
    result *= fact

def factorial_1_2(number, number2):
    fact = 1
    for n in range(number+1, number2+1):
        fact *= n
    global result
    result *= fact

def processing(n):
    global result
    if n in [0, 1]:
        result = 1
    else:
        list_cache = list(cache.keys())
        list_cache_n = [ x for x in list_cache if x<n]
        if list_cache_n==[]:
          result = 1
          number0 = 1
          number = n // 2
          number2 = n
        else:
          cache_n = max(list_cache_n)
          result = cache[cache_n]
          number0 = cache_n+1
          number = number0 + (n-cache_n)//2
          number2 = n

        thread = threading.Thread(target=factorial_1_1, args=(number0, number))
        thread2 = threading.Thread(target=factorial_1_2, args=(number, number2))

        thread.start()
        thread2.start()
        thread.join()
        thread2.join()
    if n not in cache:
      cache[n] = result
    if n>1000:
        res = str(cache[n])
        return res[:5]
    else:
        return str(cache[n])

result = 1
cache = cachetools.LRUCache(maxsize=100)