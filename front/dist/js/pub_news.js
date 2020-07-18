function News() {

}

News.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor",{
        'serverUrl': '/ueditor/upload/'
    });
};

News.prototype.listenUploadFileEvent = function () {
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file',file);
        xfzajax.post({
            'url': '/cms/upload_files/',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if(result['code'] === 200){
                    var url = result['data']['url'];
                    var thumbnailInput = $("#thumbnail-form");
                    thumbnailInput.val(url);
                }
            }
        });
    });
};

News.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');
        var tt = btn.attr('data-news-title');
        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();

        var url ='/cms/add_news/';
        console.log(tt);
        console.log(pk);
        console.log('xxxxx');


        window.setTimeout(5000);
        xfzajax.post({
            'url': '/cms/add_news/',
            'data': {
                'title': title,
                'category': category,
                'image': thumbnail,
                'content': content,
                'desc': content,
                'id':pk,
            },
            'success': function (result) {
                if(result['code'] === 200){

                    window.location.reload();
                }
            }
        });
    });
};

News.prototype.run = function () {
     this.listenSubmitEvent();
     this.listenUploadFileEvent();
     this.initUEditor()
};


$(function () {
    var news = new News();
    news.run();
});