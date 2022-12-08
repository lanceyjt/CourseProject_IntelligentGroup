var serverhost = 'http://127.0.0.1:8000';

var request = {query_input: 'world cup'}
var url = serverhost + '/intelligentgroup/search_action_analysis/?query='+ encodeURIComponent(request.query_input) ;
			
console.log(url);

fetch(url)
.then(response => response.text())
//.then(response => sendResponse({farewell: response}))
//.then(result => sendResponse({value: result}))
.then(result => console.log(result))
.catch(error => console.log(error))

