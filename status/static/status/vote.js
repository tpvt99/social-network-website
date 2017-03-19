$(document).on('click','.vote_pp', function() {
    var $this = $(this);
    $.ajax({
        method : 'GET',
        url : '/status/vote/',
        data : {'id':$this.find('.vote-p')[0].dataset.stat},
        dataType : 'json',
        success : function(data) {
            if(data.a == true) {
                $this.find('.vote-p').addClass('vote-p-co');
            }
            else {
                $this.find('.vote-p').removeClass('vote-p-co');
            }
            $this.find('.vote-count').html(data.vote);
            $this.find('.vote-quan').html(data.quan);
        }
    });
});
