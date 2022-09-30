function maxZeros(nums){
    let largest = 0;
    let current = 0;
    for (let i = 0; i<nums.length; i++) {
        if (nums[i] == 1) {
            current = 0;
        } else {
            current++;
        };
        if (current > largest){
            largest = current;
        };
    };
    console.log(largest); // 請用你的程式補完這個函式的區塊
    }
    maxZeros([0, 1, 0, 0]); // 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
    maxZeros([1, 1, 1, 1, 1]); // 得到 0
    maxZeros([0, 0, 0, 1, 1]) // 得到 3