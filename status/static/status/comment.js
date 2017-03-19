$(document).on('submit','.comment-form', function(e) {
    e.preventDefault();
    var $this = $(this);
    var form = new FormData($(this)[0]);
    if(form.get('comment').trim() === '') return false;
    var csrftoken = getCookie('csrftoken');$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/status/comment/',
        data : form,
        processData : false,
        contentType : false,
        success : function(data) {
            if (data !== 'error') {
                console.log(data);
                $this.parents('.stat-comment-post').siblings('.stat-comment').append(data);
                $this.find('.com-in').val('');
            }
        }
    });
});
