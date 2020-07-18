
// 用来处理导航条的
function FrontBase() {}


FrontBase.prototype.run = function () {
    var self = this;
    self.Listenchose();

};


FrontBase.prototype.Listenchose = function () {
    var url = window.location.href;
    var protocol = window.location.protocol;
    var host = window.location.host;
    var domain = protocol+ '//' +host;
    var path = url.replace(domain,'')
    var Navilis = $(".nav li");
    console.log(url)
    Navilis.each(function (index,element) {
        var li = $(element);
        var aTag = li.children("a");
        var href = aTag.attr("href");
        if (href === path){
            li.addClass('active');
            return false
        }
    })
};


$(function () {
    var auth = new  FrontBase();
    auth.run();
});



