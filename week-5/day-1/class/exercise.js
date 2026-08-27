// function countExercise(studentObject) {
//     total_exercise = 0
//     listOfValues = Object.values(studentObject)
//     console.log(listOfValues)
//     for (num of listOfValues) {
//         total_exercise += num
//     }
//     return total_exercise



const nick = {
    week1: 1,
    week2: 0,
    week3: 2,
    week4: 0,
    week5: 4,
    week6: 3,
    week7: 7,
    week8: 20,
}

const rose = {
    week1: 3,
    week2: 12,
    week3: 10,
    week4: 10,
    week5: 10,
    week6: 10,
    week7: 10,
    week8: 10
}

// console.log(countExercise(nick));
// console.log(countExercise(rose));

const sumTotal = (studentObject) => { return Object.values(studentObject).reduce((total, value) => total + value, 0) }

console.log(sumTotal(nick));
console.log(sumTotal(rose));

const schedule = {
    work: [8, 4, 8, 12, 8, 0, 0],
    free: [16, 20, 12, 16, 24, 24],
    hoursSorted: function () {
        const reduceFunc = (key) => { return Object.values(this[key]).reduce((total, value) => total + value, 0) }
        return `Total hours of work:  ${reduceFunc("work")} Total hours of freetime: ${reduceFunc("free")}`
    }
}

console.log(schedule.hoursSorted())

