const myName = 'Vova'

console.log(myName)

const objectA = {
    a: 10,
    b: true
}

const copyOfA = objectA
copyOfA.a = 20
copyOfA.c = 'abc'

const a = () => {
    console.log('Hey there')
}


const myCity = {
    city: 'New York'
}
myCity.popular = true
console.log(myCity)

myCity.country = 'USA'
console.log(myCity)

delete myCity.country
console.log(myCity)