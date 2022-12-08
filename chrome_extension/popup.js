$(function(){
    $('#querysubmit').click(function(){
		var query_input = $('#query').val();
		if (query_input){
                chrome.runtime.sendMessage(
                    message = {query_input: query_input},
                    function(response) {
                        result = response.farewell;
                        alert(result['bm25_scores'])
                    }
                    );
		}
		$('#query').val('');
    });
});