const express = require('express')
const app = express()
const posts = require('./data.js')

app.listen(3000, () => {
    console.log('server is listening on port 3000')
})


app.get('/api/posts', (req, res) => {
    res.json(posts)
})

app.get('/api/posts/:postID', (req, res) => {
    const postID = req.params.postID
    const post = posts.find(p => p.id === Number(postID))

    if (!post) {
        return res.status(404).json({ message: 'Post not found'})
    }
    res.json(post)
})

app.get('/api/search', (req, res) => {
    const titleQuery = req.query.title.toLowerCase()
    const filteredPosts = posts.filter(p => p.title.toLowerCase().includes(titleQuery))

    if (filteredPosts.length === 0) {
        return res.json({ message: 'No matching posts found'})
    }
    res.json(filteredPosts)
})