$(document).on('click', '.prip_p', function() {
    var $this = $(this);
    var stat = $(this)[0].dataset.stat;
    var privacy = $(this)[0].dataset.privacy;
    var csrftoken = $this.parent('.stat_pri').find("input[name='csrfmiddlewaretoken']").val();
    $.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});
    $.ajax({
        method : 'POST',
        url : '/status/update/privacy/',
        data: {'id':stat,'privacy':privacy},
        success: function(data) {
            if (data === 'ok') {
            if(privacy === 'public') {
                $this.parents('span.dropdown').find('span.rensp_pr').empty().append('<span class="fa fa-globe"></span>');
            } else if(privacy === 'friend') {
                $this.parents('span.dropdown').find('span.rensp_pr').empty().append('<span class="ion ion-person-stalker"></span>');
            } else{
                $this.parents('span.dropdown').find('span.rensp_pr').empty().append('<span class="fa fa-lock"></span>');
            }
            }
        }
    });
});
