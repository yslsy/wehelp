def avg(data):
    sum=0 #職位不是manager的總薪資
    n1=0 #職位不是manager的人數
    for n in range(len(data["employees"])):
        if data["employees"][n]["manager"] == False :
            sum = sum + data["employees"][n]["salary"]
            n1+=1
        result = sum / n1
    print(result)
# 請用你的程式補完這個函式的區塊
avg({
    "employees":[
        {
           "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式
