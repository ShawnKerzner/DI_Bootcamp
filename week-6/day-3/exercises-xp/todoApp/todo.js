export class TodoList  {
    constructor(tasks={}) {
        this.tasks = tasks;
    }

        addTask(key, value) {
            this.tasks[key] = value;
        }

        markTaskComplete(key) {
            this.tasks[key] = "Complete";
        }

        listAllTasks() {
            console.log(this.tasks);
        }
}