function AddWork() {
    $('.modal').find('.modal-content').empty().append('<p style="padding:10px 20px;text-align:center;"><span class="fa fa-circle-o-notch fa-spin fa-3x fa-fw"></span><p>');
    $('.modal').modal({
        keyborad : false,
        show : true,
    });
    $.ajax({
        method:'GET',
        url:'/profile/work/add/',
        success:function(data) {
            $('.modal').find('.modal-content').empty().append(data);
        }
    });
}
function EditWork($this) {
    $('.modal').find('.modal-content').empty().append('<p style="padding:10px 20px;text-align:center;"><span class="fa fa-circle-o-notch fa-spin fa-3x fa-fw"></span><p>');
    $('.modal').modal({
        keyborad : false,
        show : true,
    });
    $.ajax({
        method:'GET',
        url:'/profile/work/edit/',
        data : {'id':$this[0].dataset.work},
        success:function(data) {
            $('.modal').find('.modal-content').empty().append(data);
        }
    });
}
$('.add-work').on('click', function() {
    AddWork();
});
$('.edit-work').on('click', function() {
    EditWork($(this));
});
