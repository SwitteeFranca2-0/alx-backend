const kue = require('kue')
const chai = require('chai')
const expect = chai.expect
const sinon = require('sinon')
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationJobs', ()=>{
    const queue_test = kue.createQueue()
    const console_spy = sinon.spy(console)
    before(()=>{
        queue_test.testMode.enter(true);
      });
      
      afterEach(()=> {
        queue_test.testMode.clear();
        queue_test.testMode.exit();
      });
      
      after(()=> {
        console_spy.log.resetHistory();
      });
      
      it('display an error message if jobs is not an array', ()=> {
        expect(()=>createPushNotificationsJobs("it's a test", queue_test).to.throw('Jobs is not an array'))
        
    //     expect(queue.testMode.jobs[0].type).to.equal('myJob');
    //     expect(queue.testMode.jobs[0].data).to.eql({ foo: 'bar' });
    });
    it('should expect the length of jobs to be 0', ()=>{
        expect(queue_test.testMode.jobs.length).to.equal(0);     
      })
    it('should create two jobs to the queue', ()=>{
        const jobss= [
            {
              phoneNumber: '4153518780',
              message: 'This is the code 1234 to verify your account'
            },
            {
              phoneNumber: '4153518781',
              message: 'This is the code 4562 to verify your account'
            },
        ]
        createPushNotificationsJobs(jobss, queue_test)
        expect(queue_test.testMode.jobs.length).to.equal(2);     
      })
      
 
})
