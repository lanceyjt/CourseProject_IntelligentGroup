var googleUrl = window.location.toString() //'https://www.google.com/search?q=Jingtian+Is+Awesome&rlz=1C1ONGR_enUS1015US1015&oq=Jingtian+Is+Awesome&aqs=chrome..69i57j33i10i160l3.5627j0j7&sourceid=chrome&ie=UTF-8';

//Parse URL to only give search term
function getParameterByName(name,url) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(url);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

//Communicate with Python Script to get bm25, url, word frequency and topic

//Create Child Process
const spawner = require('child_process').spawn;

//Create Object to grab from python script
const data_to_pass_in =
{
    query_input:  getParameterByName('q',googleUrl), // the query input //'bm25',
    bm25_scores: undefined,
    word_freq: undefined,
    topics: undefined
};

const python_process = spawner('py', ['./main.py', JSON.stringify(data_to_pass_in)]);
python_process.stdout.on('data', (data) => {
    console.log('Data recieved from python script:', JSON.parse(data.toString()))
    });

    console.log(getParameterByName('q',googleUrl));
