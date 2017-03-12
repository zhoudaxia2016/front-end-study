var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring');
var exec = require('child_process').exec

post = 8000;
host = '127.0.0.1';
http.createServer(function(req,res){
    req.setEncoding('utf-8');
    var code = '';
    var data = '';
    //接收数据
    req.addListener('data',function(datachunk){
        data += datachunk;
    });
    //处理数据
    req.addListener('end',function(){
        console.log('数据接收完毕！');
        var params = qs.parse(data);
        exec('/usr/python3.5/bin/python3 /home/maozz/coderec/nn_predict.py CheckCode.aspx.gif',function(err,stdout,stdin){
           if (err){
              console.log('err'+stdin);
           }
           if (stdout){
              console.log(stdout);
              code = stdout;
              res.writeHead(200, {
                            "Content-Type": "text/html;charset=utf-8"
              });
              html=`<h2>你的验证码是：</h2><p style="color:blue;font-size:35px;">${code}</p>`
              res.end(html);
           }
        });
    });

}).listen(post,host);
console.log(`Server running at ${host}:${post}`);  
