$(function(){
    $('#querysubmit').click(function(){
		var query_input = $('#query').val();
		if (query_input){
                chrome.runtime.sendMessage(
                    message = {query_input: query_input},
                    function(response) {
                        url = response.url;
                        chrome.tabs.create({url: url})
                    }
                    );
		}
		$('#query').val('');
    });
});