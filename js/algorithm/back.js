//判断是否为回文字符串 

function back(str){
    return str === str.split('').reverse().join('');
}

var argv = process.argv.slice(2);
argv.forEach(function(ele){
    if (back(ele)){
        console.log(ele + '是回文字符串');
    }
    else{
        console.log(ele + '不是回文字符串');
    }
});
