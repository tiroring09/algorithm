package mylib;

import java.util.Arrays;

public class PermutationRecursiveSelected {
	static int array[], R, result[], cnt;
	static boolean[] selected;
	
	public static void main(String[] args) {
		array = new int[] {1,3,5,7,9};
		selected = new boolean[array.length];
		R = 3; // 5 P 3
		result = new int[R];
		cnt = 0;
		
		permutation(0);
//		permutation_jungbok(0);
		
		System.out.println(cnt);
	}
	
	public static void permutation(int idx) {
		if (idx == result.length) {	// 기저조건: 다 채워서 완성됨
			System.out.println(Arrays.toString(result));	// 원하는 연산 수행
			++cnt;
			return;
		}
		
		for (int i = 0; i < array.length; i++) {	// i범위는 array의 모든 인덱스 순회
			if (selected[i]) continue;	// 중복방지 조건: i인덱스가 이미 사용되었으면, 사용할 수 없으니 다음 인덱스로 넘어간다.
			
			result[idx] = array[i];	// 선택: array의 i번째 원소를 result의 idx자리로
			
			selected[i] = true;
			permutation(idx + 1);
			selected[i] = false;
		}
	}
	
	// 중복순열 = N의 R승
	public static void permutation_jungbok(int rsltIdx) {
		if (rsltIdx == R) {
			System.out.println(Arrays.toString(result));
			++cnt;
			return;
		}
		
		for (int i = 0; i < array.length; i++) {
			result[rsltIdx] = array[i];
			permutation_jungbok(rsltIdx + 1);
		}
	}

}
