$(document).ready(function(){
    // alert('자바스크립트 파일이 실행되었습니다.');
    load();
});

function load() {
    $.ajax({
        url: '/test/get/data?username=sparta&password=1234',
        type: 'get',
        data: {},
        success: function(response){
            console.log(response);
        }
    })
}

function postData() {
    $.ajax({
        url:'/test/post/data',
        type: 'post',
        data: {
            username: 'sparta',
            password: '1234'
        },
        success: function(response){
            console.log(response);
        }
    })
}