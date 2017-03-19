(function() {
    var x = $('#middle1').find('#mipic');
    if (x.data('load') === 'ano') {
        x.attr('src', '/static/web/user.jpeg');
    }
    else {
        $.ajax({
            method : 'GET',
            url : x.data('href'),
            data : {'id':x.data('user')},
            success : function(data) {
                x.attr('src',data);
            }
        });
    }
})();
