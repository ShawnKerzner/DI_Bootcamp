import express from 'express';

const router = express.Router();

const todos = [];
let taskNum = 0;

router.get('/', (req, res) => {
    res.json(todos);
});

router.post('/', (req, res) => {
    if (!req.body.task) {
        res.status(400).json({ error: "To-do is missing task" });
        return;
    }

    taskNum += 1;

    const newTodo = {
        id: taskNum,
        task: req.body.task
    }

    todos.push(newTodo);
    res.status(201).json(newTodo);
});

router.put('/:id', (req, res) => {
    const id = Number(req.params.id);
    const todo = todos.find(todo => todo.id === id);

    if(!todo) {
        return res.status(404).json({ error: "To-do not found" });
    }
    todo.task = req.body.task;
    res.json(todo);
});

router.delete('/:id', (req, res) => {
    const id = Number(req.params.id);
    const index = todos.findIndex(todo => todo.id === id);

    if (index === -1) {
        return res.status(404).json({ error: "To-do not found" });
    }

    todos.splice(index, 1);
    res.json({ message: "To-do deleted"});
});


export default router;