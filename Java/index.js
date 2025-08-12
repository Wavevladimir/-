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

a()

a = 10