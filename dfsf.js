let fibonucci = [0,1]
for (let i = 2;i<10;i++){
    fibonucci[i] = fibonucci[i-1] + fibonucci[i-2];
}
console.log(fibonucci)


function fibo(n){
    if(n==0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    return fibo(n-1) + fibo(n-2);
}
console.log(fibo(9));


function fibonucciseries(n){
    if(n==0){
        return [0];
    }
    if(n==1){
        return [0,1];
    }
    let fibo = fibonucciseries(n-1);
    fibo[n] = fibo[n-1] + fibo[n-2];
    return fibo
}
console.log(fibonucciseries(9));