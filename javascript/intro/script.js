// let str = 'Hello World!'

// console.log(str.replace(/o/g, '---'))
//  console.log(`Message: ${5 * 10}`)

// ncrement
// let x = 5
// console.log(x++)
// console.log(++x)

// console.log("123" == 123) // Auto type conversion

// person = {
//     name: 'Matt',
//     age: 50
// }
// console.log(person.name)

x = [1, 2, 3.14159, true, 'hello']

console.log(x.includes('fdadfad'))

// Python
// def add(x, y): 
//   return x + y

// function add(x, y) {
//     return x + y
// }

// const numbers = [12, 50, 44, 32, 2]

// const Utils = {
//     add: (x, y) => x + y,
//     doubler: arr => arr.map(x => x * 2)
// }

// console.log (Utils.add(5, 10))
// console.log(Utils.doubler(numbers))

// const people = ['Matt', 'Glen', 'Mary', 'Kate']

// const [,second, third, ...others] = people

// console.log(second, third, others)

const bobBirds = ['Robin', 'Crew']
const sallyBirds = ['Bluejay', 'Cardinal']

const allBirds = [...bobBirds, ... sallyBirds, 'Magpie']

console.log(allBirds)