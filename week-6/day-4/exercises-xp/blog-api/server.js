const express = require("express");
const app = express();
const posts = [
    {
        id: 1,
        title: "Blog 1",
        content: "Word + Combo = Wombo"

    },
    {
        id: 2,
        title: "Blog 2",
        content: "Peak + Cinema + Analysis = Peanemis"

    },
    {
        id: 3,
        title: "Blog 3",
        content: "Huzz + Auditorium = Huzzitorium"

    }
]


app.listen(3000, () => {
    console.log("server is listening on port 3000...");
});

app.use(express.json());

app.get('/posts', (req, res) => {
    res.status(200).json(posts)
})

app.get('/posts/:id', (req, res) => {
    const matchedPost = posts.find((post) => {
        return Number(req.params.id) === post.id
    });
    if(!matchedPost) {
        res.status(404).json({ message: "Post not found" });
    } else {
        res.status(200).json(matchedPost);
    }
})

app.post('/posts', (req, res) => {
    const justIdArray = posts.map((post) => {
        return post.id;
    });
    const newId = Math.max(...justIdArray) + 1;
    const newPost = {id: newId, title: req.body.title, content: req.body.content};
    posts.push(newPost);
    res.status(201).json(newPost);
})

app.put('/posts/:id', (req, res) => {
    const postIndex = posts.findIndex((post) => {
        return Number(req.params.id) === post.id;
    });
    if (postIndex === -1) {
        res.status(404).json({ message: "post not found"})
    } else {
        const updatedPost = {id: posts[postIndex].id, title: req.body.title, content: req.body.content};
        posts[postIndex] = updatedPost;
        res.status(200).json({ message: "post updated" });
    }
})

app.delete('/posts/:id', (req, res) => {
    const postIndex = posts.findIndex((post) => {
        return Number(req.params.id) === post.id;
    });
    if (postIndex === -1) {
        res.status(404).json({ message: "post not found"})
    } else {
        posts.splice(postIndex, 1);
        res.status(200).json({ message: "post deleted" })
    }
})

app.use((req, res) => {
    res.status(404).json({ message: "route not found" });
})