window.onload = function(){
    var cookies = document.cookie.split(/\s*;\s*/);
    cookies = cookies.map(function(v){
        return v.split('=');
    });
    var index = cookies.findIndex(function(v){
        return v[0] == 'islogin';
    });
    if (index != -1){
        if (cookies[index][1] === 'true'){
            var p = document.getElementsByClassName('login')[0];
            var a = p.getElementsByTagName('a')[0];
            a.innerText = '退出';
            a.href = '/login/logout';
        }
    }
};
