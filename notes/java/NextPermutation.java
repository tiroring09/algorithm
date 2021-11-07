package mylib;

import java.util.Arrays;

public class NextPermutation {
	static int array[], count;
	
	public static void main(String[] args) {
		array = new int[] {1, 2, 3, 4};
		count = 0;
		
		do {
			System.out.println(Arrays.toString(array));
		} while (nextPermutation());
		
		System.out.println(count);
	}
	
	static boolean nextPermutation() {
		++count;
		// 꼭지구하기
		int i = array.length-1;
		while (i > 0 && array[i-1] >= array[i]) --i;	// i==0이면 인덱스아웃
		
		// 탈출조건
		if (i == 0) return false;
		
		// i-1보다 큰 최초의 j구하기, 기저조건이 i이기때문에 걱정ㄴㄴㄴ
		int j = array.length-1;
		while(array[i-1] >= array[j]) --j;
		
		// i-1과 j swap
		int swap = array[i-1];
		array[i-1] = array[j];
		array[j] = swap;
		
		// i부터 끝까지 배열뒤집기
		j = array.length-1;
		while(i<j) {
			swap = array[i];
			array[i] = array[j];
			array[j] = swap;
			
			++i;
			--j;
		}
		
		return true;
	}
}
