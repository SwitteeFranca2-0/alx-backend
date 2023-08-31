const kue = require('kue')
const queue = kue.createQueue({
    prefix: 'q',
    redis: {
      port: 6379,
      host: 'localhost'
    }
  });

const sendNotification = (phoneNumber, message) =>{
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('push_notification_code', (job, done) =>{
    sendNotification(job.data.phoneNumber, job.data.message)
})
