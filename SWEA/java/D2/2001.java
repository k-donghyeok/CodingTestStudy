//22:23

// 완전탐색 을 2x2 크기로 하면서 최대값 갱신
// 현재 좌표에서 우 하 우 대각선 하 좌표를 dx dy로 탐색
// 반복문의 범위는 0부터 n-(m-1) 까지 

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
  public static void main(String [] args) throws Exception{
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T=Integer.parseInt(br.readLine());

    for(int test_case=1;test_case<T+1;test_case++){
      StringTokenizer st= new StringTokenizer(br.readLine());
      int n= Integer.parseInt(st.nextToken());
      int m= Integer.parseInt(st.nextToken());

      int arr[][]=new int[n][n];

      for(int y=0;y<n;y++){
        st= new StringTokenizer(br.readLine());
        int x=0;
        while(st.hasMoreTokens()){
          arr[y][x]=Integer.parseInt(st.nextToken());
          x++;
        }
        
      }

      for(int y=0;y<n;y++){
        for(int x=0;x<n;x++){
          System.out.printf("%d ",arr[y][x]);
        }
        System.out.println();
      }

      
      int max=0;
      for(int y=0;y<n-(m-1);y++){
        
        for(int x=0;x<n-(m-1);x++){
          int temp=0;
          
          for(int ny=y;ny<y+m;ny++){
            for(int nx=x;nx<x+m;nx++){
              temp+=arr[ny][nx];
            }
          }
          
          if(temp>max)max=temp;
          
        }

        
      }
      System.out.printf("#%d %d\n",test_case,max);
    }
  }
}
