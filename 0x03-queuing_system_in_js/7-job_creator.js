const kue = require('kue');
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
];

const push_notification_code_2 = kue.createQueue({
    prefix: 'q',
    redis: {
        port: 6379,
        host: 'localhost'
    },
  })

  for (const data of jobs) {
    const job = push_notification_code_2.create('push_notification_code_2', data)
    .on('enqueue', ()=>console.log('Notification job created: ', job.id))
    .on('failed', () => console.log(`Notification job ${job.id} failed`))
    .on('job complete', ()=> console.log(`Notification job ${job.id} completed`))
    .on('progress', (progress, _data)=> console.log(`Notification job ${job.id} ${progress}% completed`))
    job.save()
  }
