$('.middle_sta').on('keydown','.com-in', function(e) {var $this = $(this);if(e && e.keyCode == 13) {e.preventDefault();var des = $this.val();var ano =$this.parents('.com-create').find('a#dLabel')[0].dataset.ano;var stat = $(this).data('stat');if( des.trim() === '') return false;var csrftoken = getCookie('csrftoken');$.ajaxSetup({beforeSend: function(xhr, settings) {if (!csrfSafeMethod(settings.type) && !this.crossDomain) {xhr.setRequestHeader('X-CSRFToken', csrftoken);}}});$this.css({'opacity':'0.4'}).prop('disabled','true').val('').siblings('span').show();$.ajax({method : 'POST',url : '/anonymous/comment/',data : {'des':des,'ano':ano,'stat':stat},success: function(data) {$this.parents('.stat_comments').find('.s-co').prepend(data);$this.css({'opacity':'1'}).prop("disabled",false).siblings('span').hide();}}); }});
