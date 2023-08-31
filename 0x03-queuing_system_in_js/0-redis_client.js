import { createClient } from 'redis';
const port = 6379
const host = 'localhost'
const client = createClient(port, host);

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () =>{
  console.log('Redis client connected to the server')
})
