var http = require('http');

http.createServer(function (req, res) {
    console.log('Request received: ');
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    req.on('data', function (chunk) {
        console.log('GOT DATA!');
    });
    res.end('callback(\'{\"code\": \"'+code+'\"}\')');
    }).listen(8000,'127.0.0.1');
console.log('Server running on port http://127.0.0.1:8000/');
