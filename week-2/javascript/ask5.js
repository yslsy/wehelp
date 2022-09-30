function twoSum(nums, target){
        let n = nums.length
        for (let i = 0;i<n;i++){
            for (let j =0; j<n;j++){
                if (nums[i] + nums[j+1] === target){
                    return [i,j+1];
                };
            }
        } // your code here
    }
    let result=twoSum([2, 11, 7, 15], 9);
    console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
    