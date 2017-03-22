function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
$('.reg-form').on('submit', function() {
    if($('#idregff').val().trim() === '') {
        alert('Họ còn trống');
        return false;
    }
    if($('#idregfl').val().trim() === '') {
        alert('Tên còn trống');
        return false;
    }
    if($('#idrege').val().trim() === '') {
        alert('Email còn trống');
        return false;
    } else {
        if (validateEmail($('#idrege').val()) === false) {
            alert('Địa chỉ email không hợp lệ');
            return false;
        } 
    }
    if($('#idregp').val().trim() === '') {
        alert('Mật khẩu còn trống');
        return false;
    } else { 
        if($('#idregp').val().length < 6) {
            alert('Mật khẩu tối thiểu 6 kí tự');
            return false;
        }
    }
    if($('input[name="sex"]:checked').val() === undefined) {
        alert('Giới tính chưa chọn');
        return false;
    }
    return true;
});
