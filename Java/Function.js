let a = 5
let b = 3

function sum(a, b) {
    const c = a + b
    console.log(c)
}

sum(a, b)

a = 8
b = 12

sum(a, b)

function myFn(a, b) {
    let c
    a = a + 1
    c = a + b
    return c
}

myFn(10, 3)

function myFn() { }
myFn() // undefined

const personOne = {
    name: 'Bob',
    age: 21
}

function increasePersonAge(person) {
    person.age += 1
    return person
}

increasePersonAge(personOne)
console.log(personOne.age)

const personOne = {
    name: 'Vova',
    age: 28
}

function increasePersonAge(person) {
    const updatedPerson = Object.assign({}, person)
    updatedPerson.age += 1
    return updatedPerson
}

const updatedPersonOne = increasePersonAge(personOne)
console.log(personOne.age)
console.log(updatedPersonOne.age)