let myArr = [1,2,3,4, 5];

let coin = [0.01, 0.05, 0.1, 0.25];
// forEach array function

let doSomething = (element) => {console.log(element)};

// let doSomething = function(element){
//     console.log(element);
// }

// myArr.forEach(
//     (element) => {console.log("this is the element", element)}
// )

let totalSum = 0;

function addToTotal(element){
   totalSum += element; 
}

myArr.forEach(
    doSomething
)

coin.forEach(
    doSomething
)

coin.forEach(
    addToTotal
)

console.log("this is totalSum ",totalSum)

// map

// let multiptlyByTwo = (element) => { return element*2 };

// let doubledArr = myArr.map(multiptlyByTwo);
// console.log(doubledArr);


let fiftyCoin = (element) => { return element * 50 };
let coinMap = coin.map(fiftyCoin);
console.log(coinMap);

// filter
// let isEven = (number) => { return (number % 2 == 0) };
// let isOdd = (number) => { return (number % 2 == 1) };

// let evenElements = myArr.filter(isEven);
// let oddElements = myArr.filter(isOdd);

// console.log(evenElements)
// console.log(oddElements)

let isGreaterThanADollar = (number) => { return (number > 1) };
let filterMap = coinMap.filter(isGreaterThanADollar);
console.log(filterMap)

// for(i = 0; i < myArr.length; i++) {
//     console.log("hello element " + myArr[i]);
// }