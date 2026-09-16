const http  =require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html'});
        res.end('<h1>Welcome to MY Server</h1>');
    } else if (req.url === '/about') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end('<h1>About Page</h1><p>This is the about page.</p>');
    } else if (req.url === '/contact') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end('<h1>Contact Page</h1><p>Reach us at test@example.com</p>');
    } else if (req.url === '/help') {
        res.writeHead(200, { 'Content-Type': 'text/html'});
        res.end('<h1>Help Page</h1><p>We both know you are not going to read the help articles so just go to the contact page and ask for help there.</p>')
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html'});
        res.end('<h1>404 - Page Not Found</h1>');
    }
        
});

server.listen(3000, () => {
    console.log('Server running on http://localhost:3000')
});