package mergesort;

public interface Sorting<T extends Comparable<T>> {
	
	void sort(T[] array);
	
	void sort(T[] array, int leftIndex, int rightIndex);
}