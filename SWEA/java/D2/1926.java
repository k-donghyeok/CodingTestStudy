//22:26

// "25" 이걸 2 5 이렇게 나눠서 배열에 저장이 가능할까?

import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution{
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String num=br.readLine();
    
    for(int i=1;i<=Integer.parseInt(num);i++){
      String temp=String.valueOf(i);
      int count=0;
      for(int j=0;j<temp.length();j++){
        
        if(Integer.parseInt(String.valueOf(temp.charAt(j)))%3==0 && Integer.parseInt(String.valueOf(temp.charAt(j))) !=0 ){
          count++;
        }
      }

      for(int k=0;k<count;k++){
        System.out.printf("-");
      }
      
      
      if(count==0){
        System.out.printf("%d ",i);
      }else{
        System.out.printf(" ");
      }
    }
    
  }
}

