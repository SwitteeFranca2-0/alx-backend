const redis = require('redis')
const port = 6379
const host = 'localhost'
const util = require('util');
const client = redis.createClient(port, host)

client.on('error', err => console.log('Redis client not connected to the server: ', err));
const hgetall = util.promisify(client.hgetall).bind(client);
const hset = util.promisify(client.hset).bind(client);

const hSet= {
    "Portland":50, "Seattle": 80, "New York": 20, "Bogota": 20,
    "Cali": 40, "Paris": 2
}


async function input_dict(dict) {
    const keys = Object.keys(dict)
    for (const i in keys){
        await hset("HolbertonSchools", keys[i], dict[keys[i]])
        redis.print('Reply: 1')
    }
    const output = await hgetall("HolbertonSchools")
    console.log(output)
}

input_dict(hSet)
