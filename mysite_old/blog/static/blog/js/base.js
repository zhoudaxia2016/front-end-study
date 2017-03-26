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
      var closebtns = document.getElementsByClassName('close');
      for(let i=0, len=closebtns.length; i<len; i++){
        closebtns[i].click();
      }
    };
    document.getElementsByClassName('close')[0].onclick = function(){
        document.getElementsByClassName('cover')[0].style.display = 'none';
        this.parentNode.style.display = 'none';
    };
    document.getElementsByClassName('close')[1].onclick = function(){
        document.getElementsByClassName('cover')[0].style.display = 'none';
        this.parentNode.style.display = 'none';
    };

    document.getElementsByClassName('login')[0].onclick = function(){
        document.getElementsByClassName('login-window')[0].style.display = 'block';
        document.getElementsByClassName('cover')[0].style.display = 'block';
    };

    document.getElementById('sign-up-btn').onclick = function(){
      document.getElementsByClassName('login-window')[0].style.display = 'none';
      document.getElementsByClassName('signup-window')[0].style.display = 'block';
    };

    document.getElementsByClassName('signup-window')[0].onsubmit = function(){
      if (ensureUsername(document.getElementsByClassName('user-input')[1]) && ensurePasswd(document.getElementsByClassName('passwd-ensure')[0])){
          return true;
      }
      else {
          return false;
      }
    };

    document.getElementsByClassName('passwd-ensure')[0].onchange = function(){
      ensurePasswd(this);
    };
    document.getElementsByClassName('user-input')[1].onchange = function(){
      ensureUsername(this);
    };

};

function ensurePasswd(that){
    var passwd = document.getElementsByClassName('passwd-input')[1].value;
    if (that.value == passwd && passwd != ''){
        that.style.borderBottomColor = '#aaa';
        return true;
    }
    else{
        that.style.borderBottomColor = '#faa';
        return false;
    }
}

function ensureUsername(that){
    var username = that.value;
    if (username != ''){
        that.style.borderBottomColor = '#aaa';
        return true;
    }
    else {
        that.style.borderBottomColor = '#faa';
        return false;
    }
}
        
