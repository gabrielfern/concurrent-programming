# Some concurrent programming examples

## thread.cc -> example of how to compile it (on ubuntu/linuxmint)
> g++ -std=c++14 -pthread -o thread thread.cc -D TIME -D SAFE -D THREADS=20
