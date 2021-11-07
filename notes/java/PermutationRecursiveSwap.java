package mylib;

import java.util.Arrays;

public class PermutationRecursiveSwap {
	static int array[], result[], R, cnt=0;
	
	public static void main(String[] args) {
		array = new int[] {1,3,5,7,9};
		R = 3;
		
		permutation(0);
		System.out.println(cnt);
	}
	
	static void permutation(int idx) {
		if (idx == R) {	// 탈출조건: 선택완료
			
			result = new int[R];
			for (int x=0; x<R; x++) result[x] = array[x];
			System.out.println(Arrays.toString(result));
			
			++cnt;
			return;
		}
		
		for (int i = idx; i < array.length; i++) {
			swap(i, idx);	// 꼭함수로 뺄 필요는 없다. 파이썬이었다면 코드 한 줄로 스왑가능했음
			permutation(idx+1);
			swap(i, idx);
		}
	}
	
	static void swap(int x, int y) {
		int tmp = array[x];
		array[x] = array[y];
		array[y] = tmp;
	}
}
