window.onload = function(){
    var cookie = document.cookie;
    var items = cookie.split(';');
    for(let item of items){
        if ( /^\s*page/.test(item)){
            var n = parseInt(item.split('=')[1]);
            var t = 200 + n*40;
            document.getElementsByClassName('arrow')[0].style.top = t + 'px';
        }
    }
    document.getElementsByClassName('cover')[0].onclick = function(){
        document.getElementsByClassName('close')[0].click();
    };
    document.getElementsByClassName('close')[0].onclick = function(){
        document.getElementsByClassName('cover')[0].style.display = 'none';
        document.getElementsByClassName('login-window')[0].style.display = 'none';
    };

    document.getElementsByClassName('login')[0].onclick = function(){
        document.getElementsByClassName('login-window')[0].style.display = 'block';
        document.getElementsByClassName('cover')[0].style.display = 'block';
    };
};
