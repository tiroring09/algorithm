package mylib;

import java.util.Arrays;

public class PermutationRecursiveBitmask {
	static int array[], result[], R, cnt=0;
	
	public static void main(String[] args) {
		array = new int[] {1,3,5,7};
		R = 2;	// 4 P 2
		
		result = new int[R];
		permutation(0,0);
		
		System.out.println(cnt);
	}
	
	// idx자리에 올 수를 뽑아서 기존정보 뒤에 붙이기
	static void permutation(int idx, int info) {
		if (idx == R) {	// 탈출조건: result 완성
			System.out.println(Arrays.toString(result));
			
			++cnt;
			return;
		}
		
		for (int i = 0; i < array.length; i++) {	// i의 범위: array의 인덱스
			if ((info & 1<<i) == 0) {		// i가 사용중이지 않다면
				result[idx] = array[i];	// i를 추가하고
				permutation(idx+1, info | 1<<i);		// i를 info에 담아서 다음 인덱스로 보냄
			}
		}
	}
}
