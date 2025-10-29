#include <stdio.h>
#include <stdlib.h>
int fib(int n){
  if(n == 0){
    return 0;
  }else if(n == 1){
    return 1;
  }else{
    return fib(n-1)+fib(n-2);
  }
}

int faster_fib(int n){
  if(n == 0) return 0;
  if(n == 1) return 1;
  int *fib = malloc((n+1)*sizeof(*fib));
  fib[0] = 0;
  fib[1] = 1; 
  for(int i = 2; i <= n; i++){
    fib[i] = fib[i-1] + fib[i-2];
  }
  int final = fib[n];
  free(fib);
  return final;
}

int main(){
  int my_var = faster_fib(10); 
  printf("%d\n", my_var);
  return 0;
}
