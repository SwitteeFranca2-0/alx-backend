const kue = require('kue')
const queue = kue.createQueue({
    prefix: 'q',
    redis: {
      port: 6379,
      host: 'localhost'
    }
})

const blacklisted = ['093347802', '934328495', '4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done) =>{
  job.progress(0, 100); // Initial progress

  if (blacklisted.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error); // Fail the job
  } else {
    // Simulate sending a notification
    setTimeout(() => {
      job.progress(50, 100); // Progress to 50%
      console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      done(); // Complete the job
    }, 1000); // Simulating notification time
  }
    
}

queue.process('push_notification_code_2', (job, done)=>sendNotification(job.data.phoneNumber, job.data.message,
    job, done))
