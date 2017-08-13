use std::thread;

fn main() {
    let worker = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
        }
    });

    for i in 1..10 {
        println!("hi number {} from the main thread!", i);
    }
    worker.join();
}
