
// // 点击登录按钮，弹出模态对话框
$(function () {
    $("#btn").click(function () {
        $(".mask-wrapper").show();
    });

    $(".close-btn").click(function () {
        $(".mask-wrapper").hide();
    });

    $(".auth-box").hover(function () {
        $(".user-more-boxs").show()
    },function () {
       $(".user-more-boxs").hide()
    });

});


$(function () {
    $(".switch").click(function () {
        var scrollWrapper = $(".scroll-wrapper");
        var currentLeft = scrollWrapper.css("left");
        currentLeft = parseInt(currentLeft);
        if(currentLeft < 0){
            scrollWrapper.animate({"left":'0'});
        }else{
            scrollWrapper.animate({"left":"-400px"});
        }
    });
});


function Auth() {
    var self = this;
    self.maskwrapper = $('.mask-wrapper');
}

Auth.prototype.run = function () {
    var self = this;
    self.listen();
    self.listenlogin();
    self.listenimg();
    self.listenclick();
    self.signup();
    self.listenAuthBoxHover();

};
Auth.prototype.showEvent = function(){
    var self = this;
    self.maskwrapper.show();
};

Auth.prototype.hideEvent = function(){
  var self = this;
  self.maskwrapper.hide();
};


Auth.prototype.listenAuthBoxHover = function () {
    var authBox = $(".auth-box");
    var userMoreBox = $(".user-more-box");
       authBox.click =function(){
    };
    authBox.hover(function () {
        userMoreBox.show();
    },function () {
        userMoreBox.hide();
    });
};
Auth.prototype.listen = function(){
    var self = this;
    var loginbtn = $('.signin-btn');
    var logupbtn = $('.signup-btn');
    var closebtn = $('.close-btn');
    var scrollwrapper = $('.scroll-wrapper');

    loginbtn.click(function () {
        self.showEvent();
        scrollwrapper.css({"left":0})
    })
     logupbtn.click(function () {
        self.showEvent();
         scrollwrapper.css({"left":-400})
    })
    closebtn.click(function () {
        self.hideEvent();
    })
};

Auth.prototype.listenlogin = function () {
    var signingroup = $('.signin-group');
    var telephone = signingroup.find("input[name='telephone']");
    var password = signingroup.find("input[name='password']");
    var remember = signingroup.find("input[name='remember']");

    var submitbtm = signingroup.find(".submit-btn");
    submitbtm.click(function () {
        var tel = telephone.val();
        var pas = password.val();
        var rem = remember.prop("checked");

        xfzajax.post({
            'url':'/account/login/',
            'data':{
                'telephone':tel,
                'password':pas,
                'remember':rem?1:0,
            },
            'success':function (result) {
                console.log(result);
                if (result["code"]===200){
                    console.log('sucsess');
                    window.messageBox.show("登录成功！！");
                    window.location.reload();

                }else{
                    meg = result["message"];
                    window.messageBox.show(message)

                }
            },
            'fail':function (error) {
                console.log(error)
            }
        })
    })

};

$(function () {
    var auth = new  Auth();
    auth.run();
});

Auth.prototype.listenimg = function () {
    var imgcapture = $('.imgcapture');
    imgcapture.click(function () {
        imgcapture.attr("src","/account/img_capture/"+"?random="+Math.random())
    })

};
//
// Auth.prototype.rephone = function(){
//      var phoneclick = $('.sms-captcha-btn');
//     var tlp = $('.signup-group input[name="telephone"]');
//         phoneclick.click(function () {
//         var telephone = tlp.val();
//         if(!telephone){
//             messageBox.showInfo('请输入手机号码');
//         }
//         xfzajax.get({
//             'url':'/account/send_phone/',
//             data:{
//                 'telephone':telephone
//             },
//             'success':function (result) {
//                 if (result["code"]===200){
//                     messageBox.showInfo('短信发送成功！');
//                     phoneclick.addClass('disabled');
//                     var count = 5;
//                     phoneclick.unbind('click');
//                     var timer =setInterval(function () {
//                         phoneclick.text(count+'s');
//                         count-=1;
//                         if(count<=0){
//                             clearInterval(timer);
//                             phoneclick.removeClass('disabled');
//                             phoneclick.text('发送验证码');
//
//                         }
//                     },1000)
//                 }
//             },
//             'fail':function (error) {
//                 console.log(error)
//             }
//         })
//     })
// };

Auth.prototype.reclick = function(){
    var self = this;
     var phoneclick = $('.sms-captcha-btn');
        messageBox.showInfo('短信发送成功！');
                    phoneclick.addClass('disabled');
                    var count = 5;
                    phoneclick.unbind('click');
                    var timer =setInterval(function () {
                        phoneclick.text(count+'s');
                        count-=1;
                        if(count<=0){
                            clearInterval(timer);
                            phoneclick.removeClass('disabled');
                            phoneclick.text('发送验证码');
                            self.listenclick();
                        }
                    },1000)
}

Auth.prototype.listenclick = function () {
    var self = this;
    var phoneclick = $('.sms-captcha-btn');
    var tlp = $('.signup-group input[name="telephone"]');
        phoneclick.click(function () {
        var telephone = tlp.val();
        if(!telephone){
            messageBox.showInfo('请输入手机号码');
        }else {
            console.log(telephone);
        }
        xfzajax.get({
            'url':'/account/send_phone/',
            data:{
                'telephone':telephone
            },
            'success':function (result) {
                if (result["code"]===200){
                    self.reclick();
                }
            },
            'fail':function (error) {
                console.log(error)
            }
        })
    })
};

Auth.prototype.signup = function () {
        var sub = $('.submit-btn');
        sub.click(function () {
            var tlps = $('.tlp');
            var names = $('.names');
            var pswd1s =  $('.pwd1');
            var pswd2s =  $('.pwd2');
            var capchas =  $('.dxyzm');
            var img_capchas=  $('.imgyzm');
            var tlp = tlps.val();
            var name = names.val();
            var pswd1 = pswd1s.val();
            var pswd2 = pswd2s.val();
            var capcha = capchas.val();
            var img_capcha = img_capchas.val();
            console.log(tlp);
             console.log(name);
              console.log(pswd1);
               console.log(pswd2);
                console.log(capcha);
                 console.log(img_capcha);
            if(!tlp){
                window.messageBox.showInfo('请输入手机号码！！')
            }else {
                if(!name){
                    window.messageBox.showInfo('请输入用户名！')
                }else {
                    if(pswd1 !== pswd2){
                         window.messageBox.showInfo('两次密码不一致！')
                    }else {
                         xfzajax.post({
                           'url':'/account/register/',
                                data:{
                                    'telephone':tlp,
                                    'username':name,
                                     'password1':pswd1,
                                     'password2':pswd2,
                                    'img_captcha':img_capcha,
                                    'sms_captcha':capcha,
                                 },
                              'success':function (result) {
                                 if (result["code"]===200) {
                                     messageBox.showInfo('账户注册成功，请重新登录！');
                                     window.setTimeout(5);
                                     window.location.reload();
                                 }

                                       },
                                     'fail':function (error) {
                                         console.log(error)
                                                             }
                                  })

                    }
                }
            }
        }
        )
};


Auth.prototype.lshover= function () {
    var btn = $('.user-more-boxs')


};
//
// function Auth() {
//     var self = this;
//     self.maskWrapper = $('.mask-wrapper');
//     self.scrollWrapper = $(".scroll-wrapper");
// }
//
// Auth.prototype.run = function () {
//     var self = this;
//     self.listenShowHideEvent();
//     self.listenSwitchEvent();
//     self.listenSigninEvent();
// };
//
// Auth.prototype.showEvent = function () {
//     var self = this;
//     self.maskWrapper.show();
// };
//
// Auth.prototype.hideEvent = function () {
//     var self = this;
//     self.maskWrapper.hide();
// };
//
// Auth.prototype.listenShowHideEvent = function () {
//     var self = this;
//     var signinBtn = $('.signin-btn');
//     var signupBtn = $('.signup-btn');
//     var closeBtn = $('.close-btn');
//
//     signinBtn.click(function () {
//         self.showEvent();
//         self.scrollWrapper.css({"left":0});
//     });
//
//     signupBtn.click(function () {
//         self.showEvent();
//         self.scrollWrapper.css({"left":-400});
//     });
//
//     closeBtn.click(function () {
//         self.hideEvent();
//     });
// };
//
// Auth.prototype.listenSwitchEvent = function () {
//     var self = this;
//     var switcher = $(".switch");
//     switcher.click(function () {
//         var currentLeft = self.scrollWrapper.css("left");
//         currentLeft = parseInt(currentLeft);
//         if(currentLeft < 0){
//             self.scrollWrapper.animate({"left":'0'});
//         }else{
//             self.scrollWrapper.animate({"left":"-400px"});
//         }
//     });
// };
//
// Auth.prototype.listenSigninEvent = function () {
//     var self = this;
//     var signinGroup = $('.signin-group');
//     var telephoneInput = signinGroup.find("input[name='telephone']");
//     var passwordInput = signinGroup.find("input[name='password']");
//     var rememberInput = signinGroup.find("input[name='remember']");
//
//     var submitBtn = signinGroup.find(".submit-btn");
//     submitBtn.click(function () {
//         var telephone = telephoneInput.val();
//         var password = passwordInput.val();
//         var remember = rememberInput.prop("checked");
//
//         xfzajax.post({
//             'url': '/account/login/',
//             'data': {
//                 'telephone': telephone,
//                 'password': password,
//                 'remember': remember?1:0
//             },
//             'success': function (result) {
//                 if(result["code"] == 200){
//                     self.hideEvent();
//                     window.location.reload();
//                 }else{
//                     var messageObject = result['message'];
//                     if(typeof messageObject == 'string' || messageObject.constructor == String){
//                         window.messageBox.show(messageObject);
//                     }else{
//                         // {"password":['密码最大长度不能超过20为！','xxx'],"telephone":['xx','x']}
//                         for(var key in messageObject){
//                             var messages = messageObject[key];
//                             var message = messages[0];
//                             window.messageBox.show(message);
//                         }
//                     }
//                 }
//             },
//             'fail': function (error) {
//                 console.log(error);
//             }
//         });
//     });
// };
//
// $(function () {
//     var auth = new Auth();
//     auth.run();
// });
