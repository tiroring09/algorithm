package mylib;

import java.util.ArrayList;

public class PowersetBitmask {

	public static void main(String[] args) {
		int[] array = new int[] {1,3,5,7};
		ArrayList<Integer> result;
		
		for (int i = 0; i < 1<<array.length; i++) {		// i 범위는 0부터 (2^원소수)-1까지
			result = new ArrayList<Integer>();
			for (int j = 0; j < array.length; j++) {	// j 범위는 0부터 원소수-1까지
				if ((i & 1<<j) != 0) {					// 이진수i가 2^j 와 겹치는게 있으면 j번째 원소를 포함
					result.add(array[j]);
				}
			}	// subset initiated
			
			System.out.println(result.toString());
		}

	}

}
