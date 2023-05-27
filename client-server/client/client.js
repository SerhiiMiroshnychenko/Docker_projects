const net = require('net');

const HOST = '127.0.0.1';
const PORT = 65432;

const client = new net.Socket();

client.connect(PORT, HOST, () => {
    console.log('Connected to the server');

    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter your text: ', (message) => {
        client.write(message);
    });

    client.on('data', (data) => {
        const answer = data.toString('utf8');
        console.log(`Server's echo: ${answer}`);
        if (answer === 'EXIT') {
            client.end();
            rl.close();
        } else {
            rl.question('Enter your text: ', (message) => {
                client.write(message);
            });
        }
    });

    client.on('close', () => {
        console.log('Connection closed');
    });
});