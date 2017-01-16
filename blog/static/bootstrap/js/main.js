$('.subs').on('click', function(){
	var id = $(this).data('user_id');
	$.get( '/blog/', {id: id}).done(function(resp){
		console.log(id);
	})
});
