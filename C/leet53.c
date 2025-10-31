#include <stdio.h>
// This code is the solution to LEetcode 53 in C 
// Finding the maximum sum of a sub array
// Implement Kadanes Algorithm 
int maxSubArray(int* nums, int numSize){
    int max_sum, curr_sum;
    curr_sum = 0;
    max_sum = -100000;
    if(numSize == 1){
        return nums[0];
    }
    for(int i = 0; i < numSize; i++){
        curr_sum += nums[i];
        if(curr_sum > max_sum){
            max_sum = curr_sum;
        }
        if(curr_sum < 0){
            curr_sum = 0;
        }
    }
    return max_sum;
}

int main(){
    // [5,4,-1,7,8]
    int numSize = 5;
    int myArr[numSize];
    myArr[0] = 5;
    myArr[1] = 4;
    myArr[2] = -1;
    myArr[3] = 7;
    myArr[4] = 8;
    
    maxSubArray(myArr, numSize);
    return 0;
}