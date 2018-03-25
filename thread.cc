#include <iostream>
#include <chrono>
#include <thread>
#ifdef SAFE
#include <mutex>
std::mutex locker;
#endif

#ifndef THREADS
#define THREADS 10
#endif

#ifndef SLEEP
#define SLEEP 700ms
#endif

using namespace std;


void print(int n)
{
    using namespace std::chrono_literals;
    this_thread::sleep_for(SLEEP);
#ifdef SAFE
    locker.lock();
    cout << n << endl;
#elif defined(UNSAFE)
    cout << n << endl;
#else
    cout << n;
#endif
#ifdef SAFE
    locker.unlock();
#endif
}


int main()
{
#ifdef TIME
    using namespace chrono;
    auto start = high_resolution_clock::now();
#endif

    thread threads[THREADS];
    for (int i = 0; i < THREADS; i++)
        threads[i] = thread{print, i};
    for (int i = 0; i < THREADS; i++)
        threads[i].join();
#if !defined(SAFE) && !defined(UNSAFE)
    cout << endl;
#endif

#ifdef TIME
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start).count();
    cout << duration << " ms" << endl;
#endif
}
