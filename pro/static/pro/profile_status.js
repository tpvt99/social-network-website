function getParameterByName(name, url) {
    if(!url) {
        url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"), results = regex.exec(url);
    if(!results) return null;
    if(!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

var curr_page = 0;
var hasmoreload = true;
function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight);
}

var loadScroll = function(e) {
    var page = e.data.page;
    if ( $(window).scrollTop() + $(window).height() > getDocHeight() - 200 ) {
        $(window).off('scroll');
        callAjax(page);
    }
}

function LoadAjax(page) {
    $.ajax({
        url : "/profile/content/",
        method : 'GET',
        data: {'page' :page, 'id':getParameterByName("id")},
        success : function(data) {
            if (data !== 'error') {
                $('.status').append(data);
                $(window).on('scroll', {'page':page+1}, loadScroll);
            }
            else {
                hasmoreload = false;
            }
       },
    });
}

function callAjax(page) {
    LoadAjax(page);
}
callAjax(curr_page);
