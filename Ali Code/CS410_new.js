//Create Child Process
const spawner = require('child_process').spawn;

//Create Object to grab from python script
const data_to_pass_in =
{
    query_input: 'bm25', // the query input
    bm25_scores: undefined,
    word_freq: undefined,
    topics: undefined
};

const python_process = spawner('python3', ['./main_new.py', JSON.stringify(data_to_pass_in)]);
python_process.stdout.on('data', (data) => {
    console.log('Data recieved from python script:', JSON.parse(data.toString()))
    });
    


