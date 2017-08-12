package mergesort;


import java.util.Arrays;


public class Benchmark {
	private static final Exception AssertException = new Exception("Assertion Error!");
	private static final int LENGTH = 10000000;


	public static void shuffle(Object array[]) {
		int length = array.length;

		for (int i = 0; i < length; i++) {
			int randIndex = i + (int)(Math.random() * (length - i));

			Object tmp = array[i];
			array[i] = array[randIndex];
			array[randIndex] = tmp;
		}
	}


	public static void main(String args[]) throws Exception {
		long start = System.nanoTime();

		Sorting<Integer> merge;
		if (args.length >= 1) {
			merge = new ConcurrentMergeSort<>();
		}
		else {
			merge = new MergeSort<>();
		}

		long makeTime = System.nanoTime();
		Integer[] array = new Integer[LENGTH];
		Integer[] array2 = new Integer[LENGTH];
		makeTime = System.nanoTime() - makeTime;

		if (!Arrays.equals(array, array2)) {
			throw AssertException;
		}

		long populateTime = System.nanoTime();
		for (int i = 0; i < LENGTH; i++) {
			array[i] = i;
			array2[i] = i;
		}
		populateTime = System.nanoTime() - populateTime;

		long shuffleTime = System.nanoTime();
		shuffle(array);
		shuffleTime = System.nanoTime() - shuffleTime;

		if (Arrays.equals(array, array2)) {
			throw AssertException;
		}

		long sortTime = System.nanoTime();
		merge.sort(array);
		sortTime = System.nanoTime() - sortTime;

		if (!Arrays.equals(array, array2)) {
			throw AssertException;
		}

		System.out.printf("Make time: %13.6f\n", makeTime/1000000000.0);
		System.out.printf("Populate time: %9.6f\n", populateTime/1000000000.0);
		System.out.printf("Shuffle time: %10.6f\n", shuffleTime/1000000000.0);
		System.out.print("\033[1;36m");
		System.out.printf("Sort time: %13.6f\n", sortTime/1000000000.0);
		System.out.print("\033[1;31m");
		System.out.printf("Total time: %12.6f\n", (System.nanoTime()-start)/1000000000.0);
		System.out.print("\033[;1m");
	}
}
