// 去重

function unique(arr){
    var ret = [];
    for(var i=0; i<arr.length; i++){
        if (i === arr.indexOf(arr[i])){
            ret.push(arr[i]);
        }
    }
    return ret;
}

var argv = process.argv.slice(2);
console.log(unique(argv));
