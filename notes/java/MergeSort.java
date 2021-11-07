package mylib;

import java.util.Arrays;

public class MergeSort {
	static int array[], size;
	
	public static void main(String[] args) {
		size = 4;
		array = new int[] {22, 11, 44, 33};
		
		array = mergeSort(array);
		
		System.out.println(Arrays.toString(array));
	}
	
	// 리턴값없이 void로 짜도 똑같이 돌아간다. 인자로들어오는게 객체주소이고, 객체주소를 통해 배열객체값을 직접 수정하기 때문!
	// 함수의 리턴값을 변수에 다시 할당할 필요도 없다해
	private static int[] mergeSort(int[] array) {
		if (array.length == 1) return array;
		
		int mid_idx = (int)((array.length - 1) / 2);
		
		int[] front = new int[mid_idx+1];	// front array initiation
		for (int i = 0; i <= mid_idx; i++) front[i] = array[i];
		mergeSort(front);
		
		int[] back = new int[array.length-mid_idx-1];	// back array initiation
		for (int i = 0; i < back.length; i++) back[i] = array[mid_idx+1+i];
		mergeSort(back);
		
		// merging
		int f, b, a;	// initiate index of arrays
		f = b = a = 0;
		while (true) {
			if (f == front.length && b == back.length) break;	// 탈출조건: 둘다 인덱스 out일때
			
			if (f == front.length) {
				array[a] = back[b];
				++b;
				++a;
				continue;
			}
			
			if (b == back.length) {
				array[a] = front[f];
				++f;
				++a;
				continue;
			}
			
			if (front[f] >= back[b]) {
				array[a] = back[b];
				++b;
				++a;
			} else {
				array[a] = front[f];
				++f;
				++a;
			}
		}
		
		return array;
	}
}
