const redis = require('redis')
const port = 6379
const host = 'localhost'
const client = redis.createClient(port, host);

client.on('error', err => console.log('Redis client not connected to the server: ', err));

client.on('connect', () =>{
  console.log('Redis client connected to the server')
})

const setNewSchool = (schoolName, value) =>{
    client.set(schoolName, value, (err, res)=>{
        if (err) throw err
        redis.print('Reply: OK')
    })
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, res) => {
        if (err) throw err
        console.log(res)
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
