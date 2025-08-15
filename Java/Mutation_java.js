const a = 10

let b = a
b = 30
console.log(a)
console.log(b)

const person = {
    name: 'Vova',
    age: 28
}
person.age = 22
person.isAdult = true

console.log(person.age)

const person2 = person

person2.age = 26
console.log(person.age)