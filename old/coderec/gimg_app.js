var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var exec = require('child_process').exec

post = 8000;
host = '127.0.0.1';
http.createServer(function(req,res){
    var data = '';
    req.on('data',function(dataChunk){
        data += dataChunk;
    });
    req.on('end',function(){
        var postdata = qs.parse(data);
        console.log(postdata);
        fs.writeFile('code.gif',postdata['codegif'],'binary',function(e){
            if(e) throw e;
            console.log('file saved');
        });
        res.end();
    });
}).listen(post,host);
console.log(`Server running at ${host}:${post}`);  
