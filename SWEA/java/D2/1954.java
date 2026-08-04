//21:39 ~ 21:59

//달팽이 문제
//2차원 배열을 이동하는 문제 이므로
//dx dy 로 이동을 구현하면 편리
//우 하 좌 상 으로 방향을 반복적으로 돌림
//먼저 다음칸의 좌표로 이동해서 그 좌표가
//갈수있는곳인지 값이 없는곳인지 확인후 
// 가능하면 좌표를 변하게 하고
// 다음반복문의 시작에서 배열에 값을 추가하는것으로
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.io.FileInputStream;
class exam {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T= Integer.parseInt(br.readLine());

    for(int test_case=1;test_case<T+1;test_case++){
      int n=Integer.parseInt(br.readLine());

      int [][]arr = new int[n][n];
      int direction=0;
      int []dx={1,0,-1,0};//우 하 좌 상
      int []dy={0,1,0,-1};
      int x=0;
      int y=0;
      for(int i=1;i<=n*n;i++){
        arr[y][x]=i;

        int nx=x+dx[direction];
        int ny=y+dy[direction];
        if(nx<0 || ny<0 || nx>=n || ny>=n || arr[ny][nx]!=0){
          direction++;
          direction%=4;
          
          nx=x+dx[direction];
          ny=y+dy[direction];
          x=nx;
          y=ny;

        }else{
          x=nx;
          y=ny;
        }
      }
      System.out.println("#"+test_case);
      for(int yy=0;yy<n;yy++){
        for(int xx=0;xx<n;xx++){
          System.out.printf("%d ",arr[yy][xx]);
        }
        System.out.println();
      }
    }
  }
    
  

}
  

