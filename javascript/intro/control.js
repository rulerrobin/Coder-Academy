// python
// age = 16
// if age >= 18:
//  print ('Adult')
// else:
//  print('Child')

// const age = 16

// if (age >= 18) {
//     console.log('Adult')
// } else if (age >=13) {
//     console.log('Teen')
// } else {
//     console.log('Child')
// }

// Python - Ternary Operator
// Message = 'Allowed' if age >= 18 else 'Not Allowed'

// const message = age >= 18 ? 'Allowed' : 'Not Allowed'

// python
// match name:
//  case 'Matt':
//    pass
//  case 'John':
//    pass

// const favBird = 'Crow'

// switch (favBird) {
//     case 'Raven': // Will fall through to 'You like Crows'
//     case 'Crow':
//         console.log('You like crows!')
//         break
//     case 'Robin':
//         console.log('You like robins!')
//         break
//     default: 
//         console.log('Unknown Bird')
// }

// let count = 3

// while (count > 0) {
//     console.log(count--)
// }

// Python
// for i in range(10):
//     print (i)

// Three-part for loop
// for initialiser; condition; post iteration) {}
// initialiser - executed once, prior to first iteration
// condition - executed very iteration, priot to the iteration
//

// for (let i = 1, x=0; i <= 10; i+=2, x++) {
//     console.log(i,x)
// }

// console.log("Fibonacci")
// for (let prev = 1, next = 1; next <= 1000; tmp = next, next = prev + next, prev=tmp) {
//     console.log(next)
// }

const favFoods = ['pizza', 'paste', 'tacos']
// for food in favFoods:
// for (let index in favFoods) {
//     console.log(`{parseInt(index)+1}. ${favFoods[index]}`)
// }

favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})