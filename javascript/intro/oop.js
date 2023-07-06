// Python
// class Person:
//    def __init__(name, age):
//       self.name = name
//       self.age = age

// function Person(name, age) {
//     this.name = name
//     this.age = age
//     this.greet = () => {
//         console.log(`${this.name} is ${this.age} years old.`)
//     }
// }

// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }

//     greet() {
//       console.log(`${this.name} is ${this.age}`)
//     }
// }

// const person = new Person('Matt', 50)

// person.greet()
// console.log(person)

class Rectangle {
    #width
    #height

    constructor(width, height){
        this.#width = width
        this.#height = height
    }

    get area () {
        return this.#width * this.#height
    }

    get width (){
        return this.#width
    }

    set width(value) {
        if (typeof value === 'number'){
            this.width = value
        }
    }
}

const rect = new Rectangle(10,20)
console.log(rect.area)

// Python
// class Square(Rectangle)
//    super()

class Square extends Rectangle {

    constructors(size) {
        super(size, size)
    }
}

const sqs = new Square(10)
console.log(sq.area)