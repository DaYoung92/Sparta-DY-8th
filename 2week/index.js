// 문장의 끝을 표현 ; 이제는 안 넣어도 알아서 해석해준다

// Array (파이썬에선 list)
let a =[];
a.push('A');

// object (파이썬에선 dictionary)
let b = {
    test: 123
};

console.log(b['test']);

// 값을 불러오는 또다른 방법
const {test} = b;
console.log(test);

// for문

// 다른 반복문
let B = [1,2,3,4,5];
B.map(function(i) {
    return i*3
});

console.log(B);

// 다른 반복문 2
let c = [1,2,3,4,5];
c = c.filter(funciton(i)) {
    return i < 4;
};
console.log(c);


// 누적기
let b2 = [1,2,3,4,5];
let.sum = b2.reduce(function(acc,cur) {
    // acc :  지금까지 누적된 return값
    // cur :지금 막 들어온 array 원소값 
    return = acc + cur;});
