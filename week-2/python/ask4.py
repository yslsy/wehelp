def maxProduct(nums):
    max=0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            k=nums[i]*nums[j]
            if (k<0 and n==2):
                max = k
            if(k >max):
                max = k
    print(max)
    # 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10