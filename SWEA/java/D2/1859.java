//11:24

// 오른쪽에서 왼쪽으로 가면서 자신보다 작은 값을 만나면 갱신해주고 갱신된 값과 비교해서 큰값을 만나면
//갱신 한값부터 오른쪽 까지 계산해준다
// 아 최대값이랑 최소값을 가지고 가면서 왼쪽으로 가야한다
// 최대값 보다 큰값을 만나면 그전까지 를 계산 
// 계산은 최대값 에서 모든요소들을 마이너스 하면됨
// 그럼 완전탐색으로 왼쪽으로 가면서 탐색하면됨 모든 배열을 돌때까지
// 돌면서 result 에 이익을 더해주고

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class exam{

  public static void main(String [] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T=Integer.parseInt(br.readLine());

    for(int test_Case=1;test_Case<T+1;test_Case++){
      int n= Integer.parseInt(br.readLine());
      int [] arr=new int[3];
      StringTokenizer st = new StringTokenizer(br.readLine());
      
      for(int i=0;i<n;i++){
        arr[i]=Integer.parseInt(st.nextToken());
      }

      int result=0;
      int max=arr[n-1];
      int maxIndex=n-1;
      for(int i=n-2;i>=0;i--){
        if(arr[i]>max){
          for(int j=i+1;j<n;j++){
            result+= arr[maxIndex]- arr[j];
          }
          maxIndex=i;
          max=arr[maxIndex];
        }
      }

      System.out.printf("#%d %d\n",test_Case,result);
    }
  }
}