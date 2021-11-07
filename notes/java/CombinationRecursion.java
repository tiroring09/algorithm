package mylib;

import java.util.Arrays;

public class CombinationRecursion {
	static int array[], result[], R, cnt = 0;
	
	public static void main(String[] args) {
		array = new int[] {1,3,5,7,9};
		R = 3;		// n C r
		result = new int[R];
		
//		combination(0, 0);
		combination2(array.length, R);
		
		System.out.println(cnt);
	}
	
	/**
	 * 
	 * @param idx current: input배열의 위치, 현재 호출스택의 current값 이후부터 input배열의 원소를 고를예정
	 * @param count rsltIdx: 현재 호출스택에서 담당할 result배열 인덱스
	 */
	static void combination(int idx, int count) {
		// 기저조건
		if (count == result.length) {
			System.out.println(Arrays.toString(result));
			++cnt;
			return;
		}
		
		for (int i = idx; i < array.length; i++) {
			result[count] = array[i];	// 담고
			
			combination(i+1, count+1);	// 보내
		}
	}
	
	/**
	 * [응용] n C r = (n-1) C r + (n-1) C (r-1)
	 * @param n
	 * @param r
	 */
	static void combination2(int n, int r) {
		if (r == 0) {
			System.out.println(Arrays.toString(result));
			++cnt;
			return;
		}
		
		if (n<r) return;	// 무효
		
		// 선택
		result[r-1] = array[n-1];
		combination2(n-1, r-1);
		
		// 비선택
		combination2(n-1, r);
	}
}
