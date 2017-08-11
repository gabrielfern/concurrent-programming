package mergesort;

import java.util.Arrays;

public class MergeSort<T extends Comparable<T>> implements Sorting<T> {

	@Override
	public void sort(T[] array) {
		this.sort(array, 0, array.length-1);
	}

	@Override
	public void sort(T[] array, int leftIndex, int rightIndex) {
		if (leftIndex < rightIndex) {
	        int mid = (leftIndex+rightIndex)/2;
	        sort(array, leftIndex, mid);
	        sort(array, mid+1, rightIndex);
	        merge(array, leftIndex, mid, rightIndex);
		}
	}
	
	public void merge(T[] array,  int leftIndex, int mid, int rightIndex) {
		T[] aux = Arrays.copyOfRange(array, leftIndex, rightIndex + 1);
	    mid -= leftIndex;
	    rightIndex -= leftIndex;
	    int i = 0, j = mid + 1, k = leftIndex;

	    while (i <= mid && j <= rightIndex) {
	        if (aux[i].compareTo(aux[j]) <= 0) {
	            array[k++] = aux[i++];
	        }
	        else {
	            array[k++] = aux[j++];
	        }
	    }

	    while (i <= mid) {
	        array[k++] = aux[i++];
	    }
	    
	    while (j <= rightIndex) {
	        array[k++] = aux[j++];
		}
	}
}