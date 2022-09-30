function avg(data){
    let sum = 0; //總薪水
    let n= 0; //非經理人數
    for (i=0;i<data.employees.length;i++){
        if (data.employees[i].manager == false){
            sum += data.employees[i].salary;
            n += 1;
        }
    }
    console.log(sum/n);
    
    // 請用你的程式補完這個函式的區塊
    }
    avg({
        "employees":[
            {
                "name":"John",
                "salary":30000,
                "manager":false
            },
            {
                "name":"Bob",
                "salary":60000,
                "manager":true
            },
            {
                "name":"Jenny",
                "salary":50000,
                "manager":false
            },
            {
                "name":"Tony",
                "salary":40000,
                "manager":false
            }
        ]
    }); // 呼叫 avg 函式
    