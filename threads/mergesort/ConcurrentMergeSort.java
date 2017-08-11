package mergesort;

public class ConcurrentMergeSort<T extends Comparable<T>> implements Sorting<T> {

	@Override
	public void sort(T[] array) {
		this.sort(array, 0, array.length-1);
	}

	@Override
	public void sort(T[] array, int leftIndex, int rightIndex) {
		MergeSort<T> merge = new MergeSort<>();
		int middle = (leftIndex+rightIndex)/2;
		
		Thread t = new Thread(new Runnable() {
			@Override
			public void run() {
				System.out.println("Hello, I'm the first thread");
				merge.sort(array, leftIndex, middle);
			}
		});
		Thread t2 = new Thread(new Runnable() {
			@Override
			public void run() {
				System.out.println("Hello, I'm the second thread\n");
				merge.sort(array, middle+1, rightIndex);
			}
		});

		t.start();
		t2.start();

		try {
			t.join();
			t2.join();
		} catch (InterruptedException e) {
			e.getMessage();
		}

		merge.merge(array, leftIndex, middle, rightIndex);
	}
}
