(function() {var x = $('.stat:first').find('.stat-time');x.each(function() {var ren = $(this);var sec = ren[0].dataset.time;var minx = parseInt(sec) / 60;var hourx = minx/60;var dayx = hourx / 24;var timex = new Date();timex.setSeconds(timex.getSeconds() - parseFloat(sec));ren.attr('title', [timex.getDate()," tháng ", timex.getMonth()+1, " năm ", timex.getFullYear() ," vào lúc ", timex.getHours(), " giờ ", timex.getMinutes(), " phút" ].join(''));if(sec < 60 ) {ren.html( [Math.round(sec)," giây trước"].join(''));}else if (minx < 60) {ren.html([Math.round(minx), " phút trước"].join(''));}else if( hourx < 24) {ren.html([Math.round(hourx), " giờ trước"].join(''));}else if(Math.round(dayx) <= 1) {ren.html([Math.round(dayx), " ngày trước"].join(''));}else {ren.html([timex.getDate()," tháng ", timex.getMonth()+1, " năm ", timex.getFullYear()].join(''));}});})();
