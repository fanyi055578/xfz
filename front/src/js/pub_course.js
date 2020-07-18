
function PubCourse() {

}

PubCourse.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor",{
        'serverUrl': '/ueditor/upload/'
    });
};

PubCourse.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function () {
        var title = $("#title-input").val();
        var category_id = $("#category-input").val();
        var teacher_id = $("#teacher-input").val();
        var video_url = $("#video-input").val();
        var cover_url = $("#cover-input").val();
        var price = $("#price-input").val();
        var duration = $("#duration-input").val();
        var profile = window.ue.getContent();
        console.log('hahahahahahhaha');
        xfzajax.post({
            'url': '/course/pub_course/',
            'data': {
                'title': title,
                'video_url': video_url,
                'video_img': cover_url,
                'price': price,
                'profile': profile,
                'time_lone':duration,
                'category': category_id,
                'teacher': teacher_id,
            },
            'success': function (result) {
                if(result['code'] === 200){

                    window.location = window.location.href;
                }
                else {
                    window.messageBox.showInfo('参数错误！')
                }
            },
            'fail':function (error) {
                 window.messageBox.showInfo(error)
            }

        });
    });
};

PubCourse.prototype.run = function () {
    this.initUEditor();
    this.listenSubmitEvent();
};


$(function () {
    var course = new PubCourse();
    course.run();
});