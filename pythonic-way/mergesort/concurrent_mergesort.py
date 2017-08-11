#!/usr/bin/python3
# Gabriel Fernandes


from time import time
from random import shuffle
from multiprocessing import Pool, cpu_count


def sort(array, lbound=0, rbound=None):
    if rbound == None:
        rbound = len(array)-1

    if lbound < rbound:
        def calc(leng, cpus):
            l = []
            for i in range(0, leng, leng//cpus):
                l.append([i, min(i + leng//cpus-1, leng-1)])
            if len(l) > cpus:
                l[-2][1] = l[-1][1]
                l.pop()
            return l

        def inner_merge(array, intervals, lbound, rbound):
            if lbound < rbound:
                mid = (lbound+rbound)//2
                inner_merge(array, intervals, lbound, mid)
                inner_merge(array, intervals, mid+1, rbound)
                merge(array, intervals[lbound][0], intervals[mid][1], intervals[rbound][1])

        with Pool() as pool:
            leng = rbound-lbound + 1
            works = calc(leng, cpu_count())

            workers = []
            for w in works:
                workers.append(pool.apply_async(concurrent_sort,
                                args=(array, w[0], w[1]),
                                callback=lambda t: array.
                                            __setitem__(slice(t[1], t[2]+1),
                                                        t[0][t[1]:t[2]+1])))
            for p in workers:
                p.wait()

            inner_merge(array, works, 0, len(works)-1)

    return array


def concurrent_sort(array, lbound, rbound):
    if lbound < rbound:
        mid = (lbound+rbound)//2
        concurrent_sort(array, lbound, mid)
        concurrent_sort(array, mid+1, rbound)
        merge(array, lbound, mid, rbound)

        return (array, lbound, rbound)


def merge(array, lbound, mid, rbound):
    aux = array[lbound:rbound+1]
    mid -= lbound
    rbound -= lbound
    i, j, k = 0, mid+1, lbound

    while i <= mid and j <= rbound:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
            k += 1
        else:
            array[k] = aux[j]
            j += 1
            k += 1

    while i <= mid:
        array[k] = aux[i]
        i += 1
        k += 1
    while j <= rbound:
        array[k] = aux[j]
        j += 1
        k += 1

    return (array, lbound, rbound+lbound)


def test():
    assert sort([4,3,2,1]) == [1,2,3,4]
    assert sort([4,2,3,1]) == [1,2,3,4]
    assert sort([4,5,3,2,1]) == [1,2,3,4,5]

    arr = list(range(1000))
    for _ in range(10):
        tmp = arr[:]
        shuffle(tmp)
        assert id(tmp) != id(arr)
        assert sort(tmp) == arr

    return 'test pass!'


def benchmark():
    start = time()

    list_comprehension = time()
    arr = [i for i in range(2000000)]
    list_comprehension = time() - list_comprehension

    list_copy = time()
    arr2 = arr[:]
    list_copy = time() - list_copy

    shuffle_time = time()
    shuffle(arr)
    shuffle_time = time() - shuffle_time

    not_equal_time = time()
    assert arr != arr2
    not_equal_time = time() - not_equal_time

    sort_time = time()
    sort(arr)
    sort_time = time() - sort_time

    equal_time = time()
    assert arr == arr2
    equal_time = time() - equal_time

    print('List comprehension: {:10.6f} secs'.format(list_comprehension))
    print('List copy: {:19.6f} secs'.format(list_copy))
    print('Shuffle time: {:16.6f} secs'.format(shuffle_time))
    print('Not equal time: {:14.6f} secs'.format(not_equal_time))
    print('\033[1;36m', end='')
    print('Sort time: {:19.6f} secs'.format(sort_time))
    print('\033[0;0m', end='')
    print('Equal time: {:18.6f} secs'.format(equal_time))
    print('\033[1;31m', end='')
    print('Total time: {:18.6f} secs'.format(time()-start))
    print('\033[;1m', end='')


if __name__=='__main__':
    #print(test())
    benchmark()
