const redis = require('redis')
const util = require('util');

const delay = util.promisify(setTimeout);
const port = 6379
const host = 'localhost'
const client = redis.createClient(port, host);

client.on('err', (err)=> console.log('Redis client not connected to server: ', err))
client.on('connect', ()=> console.log('Redis client connected to server') )

const publishMessage = async (message, time) =>{
    await delay(time)
    console.log(`About to send ${message}`)
    await client.publish('holberton school channel', message); 
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
