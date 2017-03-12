var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var exec = require('child_process').exec

post = 8000;
host = '127.0.0.1';
http.createServer(function(req,res){
    exec('/usr/python3.5/bin/python3 /home/maozz/std/coderec/nn_predict.py /home/maozz/dwnld/',function(err,stdout,stdin){
       if (err){
          console.log('err'+stdin);
       }
       if (stdout){
          console.log('验证码识别出来是:'+stdout);
          res.writeHead(200, { 'Content-Type': 'text/plain' });
          var code = stdout;
          res.end('callback(\'{\"code\": \"'+code+'\"}\')');
       }
    });
}).listen(post,host);
console.log(`Server running at ${host}:${post}`);  
