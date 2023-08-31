const kue = require('kue')


const data = {
    phoneNumber: "08098978654",
    message: "I named my love Habibi",
};

const push_notification_code = kue.createQueue({
    prefix: 'q',
    redis: {
      port: 6379,
      host: 'localhost'
    }
  });

const job = push_notification_code.create('push_notification_code', data)
            .save((err)=> {
                if (!err) console.log('Notification job created: ', job.id)
            });
job.on('failed', () => console.log('Notification job failed'));
job.on('job complete', ()=> console.log('Notfication job created'))
