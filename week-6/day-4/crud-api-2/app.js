const express = require("express");
const app = express();
const posts = require("./data.js")

app.listen(5000, () => {
    console.log("server is listening on port 5000...")
})

app.use(express.json());

app.post('/api/posts', (req, res) => {
    const justIdArray = posts.map((post) => {
        return post.id;
    })
    const newId = Math.max(...justIdArray) + 1;
    const newPost = {id: newId, title: req.body.title, content: req.body.content};
    posts.push(newPost);
    res.status(201).json(newPost);
    
});

app.get('/api/posts', (req,res) => {
    res.status(200).json(posts);
})

app.get('/api/posts/:postID', (req, res) => {
    const matchedPost = posts.find((post) => {
    return Number(req.params.postID) === post.id
});
    if (!matchedPost) {
    res.status(404).json({message: "Post not found" });
} else {
    res.status(200).json(matchedPost);
}
})

app.put('/api/posts/:postID', (req, res) => {
    const postIndex = posts.findIndex((post) => {
        return Number(req.params.postID) === post.id;
    })
    if (postIndex === -1) {
        res.status(404).json({message: "Post not found"})
    } else {
        const updatedPost = {id: posts[postIndex].id, title: req.body.title, content: req.body.content};
        posts[postIndex] = updatedPost;
        res.status(200).json({message: "Post updated"});
    }
})

app.delete('/api/posts/:postID', (req, res) => {
    const postIndex = posts.findIndex((post) => {
        return Number(req.params.postID) === post.id;
    })
    if (postIndex === -1) {
        res.status(404).json({message: "Post not found"})
    } else {
         posts.splice(postIndex, 1);
         res.status(200).json({message: "Post deleted"});
    }
});




