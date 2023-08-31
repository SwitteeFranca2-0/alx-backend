const redis = require('redis')
const port = 6379
const host = 'localhost'
const util = require('util');
const client = redis.createClient(port, host)

client.on('error', err => console.log('Redis client not connected to the server: ', err));
const get = util.promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) =>{
    client.set(schoolName, value, (err, res)=>{
        if (err) throw err
        redis.print('Reply: OK')
    })
}

async function displaySchoolValue(schoolName){
    const val = await get(schoolName)
    console.log(val)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
