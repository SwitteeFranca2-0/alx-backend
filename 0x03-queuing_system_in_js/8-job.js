const kue = require('kue')

const push_notification_code_3 = kue.createQueue({
    prefix: 'q',
    redis:{
        port: 6379,
        host: 'localhost'
    }
})

export default function createPushNotificationsJobs (jobs, queue){
    if (!Array.isArray(jobs)){
        throw new Error('Jobs is not an array')
    }
    jobs.forEach(data=> {
        const job = push_notification_code_3.create('push_notification_code_3', data)
        .on('enqueue', ()=>console.log('Notification job created: ', job.id))
        .on('failed', () => console.log(`Notification job ${job.id} failed`))
        .on('job complete', ()=> console.log(`Notification job ${job.id} completed`))
        .on('progress', (progress, _data)=> console.log(`Notification job ${job.id} ${progress}% completed`))
        job.save()
    })
}

