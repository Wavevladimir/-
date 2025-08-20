let a
let b

function myFn() {
    let b
    a = true
    b = 10
    console.log(b)
}

myFn()

console.log(a)
console.log(b)

const a = 5

function myFn() {
    function innerFn() {
        console.log(a) //5
    }
    innerFn()
}

myFn()

let a
let b

function myFn() {
    let b
    a = true
    b = 10
    console.log(a)
}

myFn()

console.log(a)//true
console.log(b)//undefiend