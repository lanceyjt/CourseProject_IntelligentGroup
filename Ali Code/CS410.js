//Create Child Process
const spawner = require('child_process').spawn;

//Create Object to grab from python script
const data_to_pass_in =
{
data_sent: 'Get Document URL:',
data_returned: undefined 
};

console.log('Data Sent to python script:', data_to_pass_in);
//run main.py and convert data from value to string
const python_process = spawner('python3', ['./main.py', JSON.stringify(data_to_pass_in)]);
//Grab data from python file 
python_process.stdout.on('data', (data) => {
console.log('Data recieved from python script:', JSON.parse(data.toString()))
});

const data_to_pass_in_1 =
{
data_sent_1: 'Get Word Frequency:',
data_returned_1: undefined 
};

console.log('Data Sent to python script:', data_to_pass_in_1);

const python_process_1 = spawner('python3', ['./main.py', JSON.stringify(data_to_pass_in_1)]);

python_process_1.stdout.on('data', (data) => {
console.log('Data recieved from python script:', JSON.parse(data.toString()))
});

const data_to_pass_in_2 =
{
data_sent_2: 'Get Topics:',
data_returned_2: undefined 
};

console.log('Data Sent to python script:', data_to_pass_in_2);

const python_process_2 = spawner('python3', ['./main.py', JSON.stringify(data_to_pass_in_2)]);

python_process_2.stdout.on('data', (data) => {
console.log('Data recieved from python script:', JSON.parse(data.toString()))
});

