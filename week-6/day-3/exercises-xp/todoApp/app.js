import { TodoList } from "./todo.js";

const tasks = new TodoList;

tasks.addTask("Attend Class", "Uncomplete");
tasks.addTask("Exercise XP", "Uncomplete");
tasks.addTask("Daily Challenge", "Uncomplete");

tasks.markTaskComplete("Attend Class");

tasks.listAllTasks();


