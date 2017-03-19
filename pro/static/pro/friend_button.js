$('.ev-addf').on('click', function(e) {
    e.stopPropagation();
    var $this = $(this);
    var t = $this[0].dataset.action;
    var csrftoken = $(this).parents('.profile_bg_child2').find('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/friend/add/',
        data : {'key':$this[0].dataset.who,'action':t},
        success: function(data) {
            if (data === 'ok') {
                if(t==='connect') {
                    $this.text('Hủy yêu cầu kết bạn');
                    $this[0].dataset.action = 'decline';
                } else if(t=== 'decline') {
                    $this[0].dataset.action = 'connect';
                    $this.text('Kết bạn');
                } else if(t=== 'accept') {
                    $this.text('Bạn bè');
                    $this.attr('disabled','disabled');
                    $this.siblings('.ev-addf').remove();
                } else if (t=== 'refuse') {
                    $this.text('Kết bạn');
                    $this[0].dataset.action = 'connect';
                    $this.siblings('.ev-addf').remove();
                }
            }
            else {
                alert('Có lỗi xảy ra. Xin vui lòng thử lại');
            }
        }
    });
});
