import chalk from 'chalk';
function useChalk(name, day) {
    console.log(`${chalk.green('Hello')} ${chalk.red(name)} today is ${chalk.yellow(day)}`)
}

export {useChalk};