
var dramalist = new Vue({
    el: '.drama-list',
    delimiters: ['[[',']]'],
    data: {
        dramas: [],
        show: 0,
        type: 0,
        all: true,
        allType: true,
        types: ['Am','Cn','Jp','Sk','Th'],
    },
    methods: {
        add: function(event){
            drama = {name: event.target.value, isSeen: 0, type: this.type};
            this.dramas.push(drama);
            event.target.value = '';
        },
        toggle: function(n){
            if (n === -1){ 
                this.all = true;
            }
            else{
                this.all = false;
                this.show = n;
            }
        },
        toggleType: function(n){
            if (n === -1){
                this.allType = true;
            }
            else{
                this.allType = false;
                this.type = n;
            }
        },
        isSeen: function(item){
            if (item.isSeen === 1){
                item.isSeen = 0;
            }
            else{
                item.isSeen = 1;
            }
        },
        remove: function(item){
            var ind = this.dramas.indexOf(item);
            this.dramas.splice(ind,1);
        },
        upload: function(){
            this.$http.post('/postdramas',{data: this.dramas}).then(function(res){
                console.log(res.body);
                var win = document.createElement('div');
                win.className = 'win';
                win.innerText = '上传成功';
                win.onclick = function(){
                    this.parentNode.removeChild(this);
                };
                document.body.appendChild(win);
            },function(){
                console.log('Fail!');
            });
        }
    },
    computed: {
        count: function(){
            var that = this;
            if (this.all && this.allType){
                return this.dramas.length;
            }
            else if(this.allType){
                let num = this.dramas.reduce(function(sum,item){
                    if (item.isSeen === that.show){
                        return sum += 1;
                  console.log('b');
                    }
                    else{
                        return sum;
                    }
                },0);
                return num;
            }
            else if (this.all){
                let num = this.dramas.reduce(function(sum,item){
                    if (item.type === that.type){
                        return sum += 1;
                    }
                    else{
                        return sum;
                    }
                },0);
                return num;
            }
            else{
                let num = this.dramas.reduce(function(sum,item){
                    if (item.type === that.type && item.isSeen === that.show){
                        return sum += 1;
                    }
                    else{
                        return sum;
                    }
                },0);
                return num;
            }
                
        }
    },
    mounted: function(){
        this.$http.get('/getdramas').then(res=>{this.dramas=transform(res.data.dramas)},fail);
    },
    
});

function fail(data, status, request) {
    console.log('fail' + status + "," + request);
}

function transform(data){
    var res = [];
    for(let item of data){
        res.push({name: item[0], isSeen: item[1], type: item[2]});
    }
    return res;
}

