const redis = require('redis')
const port = 6379
const host = 'localhost'
const client = redis.createClient(port, host);

client.on('err', (err)=> console.log('Redis client not connected to server: ', err))
client.on('connect', ()=> console.log('Redis client connected to server') )

const subScribe = async () =>{
    const listener = async (channel, message) =>{
        console.log(message);
        if (message === 'KILL_SERVER') {
            await client.unsubscribe(channel);
            client.quit()
        }
    } 
    await client.subscribe('holberton school channel');
    await client.on('message', listener)
}
subScribe()
