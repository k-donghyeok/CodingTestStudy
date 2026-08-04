//16:51 ~ 17:32

// 배열을 만들어서 인덱스 를 값으로 해서
// 해당 값이 나올때 마다 카운팅 하기
// 모든 값을 카운팅 후 배열에서 최대 값을 구한후
// 그값의 인덱스 를 출력
// 최빈수가 여러개 일때 에
// 가장 큰 점수를 출력을 어떻게 하지?
// 내림차순으로 정렬후 최대값의 갯수를 구한후
// 완탐으로 배열을 횟수를 만족할때 까지 돈다
// 아 뭐야 그냥 제일 오른쪽에서 오면서 찾으면되네

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class exam {
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int T=Integer.parseInt(br.readLine());

    for(int test_case=1;test_case<T+1;test_case++){
      int n=Integer.parseInt(br.readLine());
      int [] arr = new int[101];
      int max=0;
      StringTokenizer st = new StringTokenizer(br.readLine());
      while(st.hasMoreElements()){
        
        arr[Integer.parseInt(st.nextToken())]++;
      }

      for(int num : arr){
        if(num>=max){
          max=num;
        }
      }
      
      for(int i=100;i>=0;i--){
        if(arr[i]==max){
          //System.out.println(max);
          System.out.printf("#%d %d\n",test_case,i);
        }
      }

    }
  }
}
