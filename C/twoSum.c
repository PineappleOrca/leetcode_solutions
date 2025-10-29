#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 * 
 * This is the solution to the TwoSum Leetcode problem in C with test cases in the main function
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int index = 0;
    int difference = 0;
    int* result = (int*)malloc(2 * sizeof(int));
    while(index < numsSize){
        int myVar = nums[index];
        difference = target - myVar;
        for(int i = index+1; i < numsSize; i++){
            if(nums[i] == difference){
                result[0] = index;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
        }
        index += 1;
    }
    return 0;
}

int main(){
/* ---- Test case 1 ---- */
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int *res1 = twoSum(nums1, sizeof(nums1)/sizeof(nums1[0]), target1, &returnSize1);
    printf("Test 1 (target=%d)\n", target1);
    free(res1);
/* ---- Test case 2 ---- */
    int nums2[] = {3,2,4};
    int target2 = 6;
    int returnSize2;
    int *res2 = twoSum(nums2, sizeof(nums2)/sizeof(nums2[0]), target2, &returnSize2);
    printf("Test 2 (target=%d)\n", target1);
    free(res2);
/* ---- Test case 3 ---- */
    int nums3[] = {3,3};
    int target3 = 6;
    int returnSize3;
    int *res3 = twoSum(nums3, sizeof(nums3)/sizeof(nums3[0]), target3, &returnSize3);
    printf("Test 3 (target=%d)\n", target3);
    printf("Result %d , %d, Expected %d, %d", res3[0], res3[1], 0, 1);
    free(res1);
}

