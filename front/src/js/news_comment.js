function Comment() {}

Comment.prototype.PubComment = function(){
    var sbmt = $('.submits-btn');
    var textarea = $("textarea[name='comment']");
    sbmt.click(function () {
        var comment =$(".comment-textarea");
        var news_id = comment.attr('data-news-id');
        console.log(news_id);
        var content = textarea.val();


          xfzajax.post({
            'url': '/news_comment/',
            'data': {
                'comment':content,
                'news_id':news_id,
            },
            'success': function (result) {
                if(result['code'] === 200){
                    var comment = result['data'];
                    var tpl = template('comment-item',{"comment":comment});
                    var commentListGroup = $(".comment-list");
                    commentListGroup.prepend(tpl);
                    window.messageBox.showSuccess('评论发表成功！');
                    textarea.val("");
                }
            }

        });
    });
};

Comment.prototype.run = function(){
  this.PubComment();
};


$(function () {
    var x = new Comment();
    x.run()
});
