$('.profile-head').on('mouseover', function() {
    $('.head-edit').show();
}).on('mouseout', function() {
    $('.head-edit').hide();
});
$('.profile-bio').on('mouseover', function() {
    $('.bio-edit').show();
}).on('mouseout', function() {
    $('.bio-edit').hide();
});
$('.user-name').on('mouseover', function() {
    $('.name-edit').show();
}).on('mouseout', function() {
    $('.name-edit').hide();
});
function HeadBioName(x,t) {
    $('.modal').find('.modal-content').empty().append('<p style="padding:10px 20px;text-align:center;"><span class="fa fa-circle-o-notch fa-spin fa-3x fa-fw"></span><p>');
    $('.modal').modal({
        keyborad : false,
        show : true,
    });
    $.ajax({
        method:'GET',
        url:'/profile/'+x+'/?a='+t,
        success:function(data) {
            $('.modal').find('.modal-content').empty().append(data);
        }
    });
}
$('.head-add').on('click', function() {
    HeadBioName('head', 'add');
});
$('.head-edit').on('click', function() {
    HeadBioName('head','edit');
});
$('.bio-add').on('click', function() {
    HeadBioName('bio', 'add');
});
$('.bio-edit').on('click', function() {
    HeadBioName('bio','edit');
});
$('.name-edit').on('click', function() {
    HeadBioName('name','edit');
});
