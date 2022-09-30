function maxProduct(nums){
    let largest = 0;
    let current = 0;
    for (let i = 0; i<nums.length; i++) {
        for(let j =i; j<nums.length; j++){
            current = nums[i]*nums[j+1];
            if (nums.length==2 && current<0){
                largest = current;
            }
            else if (current > largest){
                largest = current;
            };
        };
    };
    console.log(largest);
    
    // 請用你的程式補完這個函式的區塊
    }
    maxProduct([5, 20, 2, 6]) // 得到 120
    maxProduct([10, -20, 0, 3]) // 得到 30
    maxProduct([10, -20, 0, -3]) // 得到 60
    maxProduct([-1, 2]) // 得到 -2
    maxProduct([-1, 0, 2]) // 得到 0 或 -0
    maxProduct([5, -1, -2, 0]) // 得到 2
    maxProduct([-5, -2]) // 得到 10
    