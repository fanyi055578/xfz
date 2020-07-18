function News() {

}


News.prototype.listenDeleteEvent = function(){
    console.log('xxxxxx');
    var delBtn = $(".delete-btn");

    delBtn.click(function () {
         event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');
        xfzajax.post({
            'url':'/cms/delete_news/',
            'data':{
                'pk':pk,
            },
            'success': function (result) {
                if(result['code']===200)
                    window.location.reload();
            },
        }
            )
    })
};

News.prototype.listenEditnews = function(){
    var Btn = $(".edit-btn");
    Btn.click(function (event) {
        event.preventDefault();
        var Btn = $(this);
        var pk = Btn.attr('data-news-id');
        console.log(pk);
        xfzajax.post({
            'url':'/cms/edit_news/',
            'data':{
                'pk':pk
            },
            'success':function (result) {
                if (result['code']===200){
                    console.log('chenggong');
                     window.location.reload()
                }

            },
            'fail':function (error) {

            }
        })
    })
};

News.prototype.initUEditor = function () {
    window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/'
    });
};


News.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    console.log('heheheh');
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');

        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        url = '/cms/tests/';
        xfzajax.post({
            'url': url,
            'data': {
                'title': title,
                'category': category,
                'desc': desc,
                'thumbnail': thumbnail,
                'content': content,
                'pk': pk
            },
            'success': function (result) {
                if(result['code'] === 200){
                    xfzalert.alertSuccess('恭喜！新闻发表成功！',function () {
                        window.location.reload();
                    });
                }
            }
        });
    });
};



News.prototype.run = function () {
     this.initUEditor();
     this.listenDeleteEvent();
     this.listenSubmitEvent();
     // this.listenEditnews();
};


$(function () {
    var news = new News();
    news.run();
});