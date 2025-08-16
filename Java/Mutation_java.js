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

#Вариант 1 по избежанию мутаций

const person = {
    name: 'Bob',
    age: 25
}

const person2 = Object.assign({}, person)

person2.age = 26

console.log(person2.age) // 26
console.log(person.age) // 25

#Вариант 2
const person = {
    name: 'Bob',
    age: 25
}

const person2 = { ...person }
person2.name = 'Alice'

console.log(person2.name) // Alice
console.log(person.name) // Bob

#Вариант 3

const person = {
    name: 'Bob',
    age: 23
}

const person2 = JSON.parse(JSON.stringify(person))

person2.name = 'Alice'

console.log(person2.name) // Alice
console.log(person.name) // Bob