package mylib;

import java.util.LinkedList;
import java.util.Queue;

public class BFS {
	static int[][] map = new int[3][3];
	static int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
	
	public static void main(String[] args) {
//		bfs1();
//		bfs2();
		bfs3();
	}
	
	static void bfs3() {
		// 0,0 ~ 2,2로 이동하는 최단 거리를 찾아보자
		// 방문했던 곳은 더 이상 가지 말자!
		boolean[][] visited = new boolean[3][3];
		// 두개 이상의 정보를 담아야 해..
		// 배열: int[] pair = {0,0} : index가 의미, 동일한 데이터 타입만 처리가능 {0, 0, true},
		// 출력이 번거롭다. 하지만 속도가 빠르고 가볍다는 장점은 있다.
		// 사용자 정의 클래스를 이용할 수도 있다.
		
		Queue<Point> q = new LinkedList<>();
		
		q.offer(new Point(0,0,0));
		visited[0][0] = true;
		
		int size = q.size();
		while(size-- > 0) {
				
				Point front = q.poll();
				
				System.out.println(front);
				
				for (int d=0; d<dirs.length; d++) {
					int nr = front.row + dirs[d][0];
					int nc = front.col + dirs[d][1];
					
					if(isIn(nr,nc)) {
						if(!visited[nr][nc]) {
							visited[nr][nc] = true;
							q.offer(new Point(nr, nc, front.depth+1));
						}
					}
				}
				
			
			
		}
		System.out.println("턴은 종료 되었고, 남은것은"+q.toString());
	}
	
	static void bfs2() {
		// 0,0 ~ 2,2로 이동하는 최단 거리를 찾아보자
		// 방문했던 곳은 더 이상 가지 말자!
		boolean[][] visited = new boolean[3][3];
		// 두개 이상의 정보를 담아야 해..
		// 배열: int[] pair = {0,0} : index가 의미, 동일한 데이터 타입만 처리가능 {0, 0, true},
		// 출력이 번거롭다. 하지만 속도가 빠르고 가볍다는 장점은 있다.
		// 사용자 정의 클래스를 이용할 수도 있다.
		
		Queue<Point> q = new LinkedList<>();
		
		q.offer(new Point(0,0,0));
		visited[0][0] = true;
		 
		while(!q.isEmpty()) {
			int size = q.size();
			for (int s = 0; s<size; s++) {
				
				Point front = q.poll();
				
				System.out.println(front);
				
				for (int d=0; d<dirs.length; d++) {
					int nr = front.row + dirs[d][0];
					int nc = front.col + dirs[d][1];
					
					if(isIn(nr,nc)) {
						if(!visited[nr][nc]) {
							visited[nr][nc] = true;
							q.offer(new Point(nr, nc, front.depth+1));
						}
					}
				}
				
			}
			System.out.println("하나의 턴이 끝났습니다.");
		}
	}
	
	static void bfs1() {
		// 0,0 ~ 2,2로 이동하는 최단 거리를 찾아보자
		// 방문했던 곳은 더 이상 가지 말자!
		boolean[][] visited = new boolean[3][3];
		// 두개 이상의 정보를 담아야 해..
		// 배열: int[] pair = {0,0} : index가 의미, 동일한 데이터 타입만 처리가능 {0, 0, true},
		// 출력이 번거롭다. 하지만 속도가 빠르고 가볍다는 장점은 있다.
		// 사용자 정의 클래스를 이용할 수도 있다.
		
		Queue<Point> q = new LinkedList<>();
		
		q.offer(new Point(0,0,0));
		visited[0][0] = true;
		
		while(!q.isEmpty()) {
			Point front = q.poll();
			
			System.out.println(front);
			
			for (int d=0; d<dirs.length; d++) {
				int nr = front.row + dirs[d][0];
				int nc = front.col + dirs[d][1];
				
				if(isIn(nr,nc)) {
					if(!visited[nr][nc]) {
						visited[nr][nc] = true;
						q.offer(new Point(nr, nc, front.depth+1));
					}
				}
			}
		}
	}

	private static boolean isIn(int r, int c) {
		return 0<=r && 0<=c && r<3 && c<3;
	}
}

class Point{
	int row, col, depth;	//

	public Point(int row, int col, int depth) {
		super();
		this.row = row;
		this.col = col;
		this.depth = depth;
	}

	@Override
	public String toString() {
		return "Point [row=" + row + ", col=" + col + ", depth=" + depth + "]";
	}
	
	
}
