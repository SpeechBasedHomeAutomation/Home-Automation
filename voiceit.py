//First use npm install VoiceIt to install our Node Library
//Then initialize it like this with your own developerId which you can find at voiceit.io/settings
myVoiceIt = require('VoiceIt');
myVoiceIt.initialize('YOUR_DEVELOPER_ID_HERE');

function startEnrollmentProcess(counter, enrollmentsDone){
  myVoiceIt.createEnrollment({
    userId: 'developerUserId',
    password: 'd0CHipUXOk',
    pathToEnrollmentWav: '/home/users/username/enroll' + counter + '.wav',
    contentLanguage: 'en-US',
    callback: function(response){
    var parsedJSON = JSON.parse(response2);
    if(parsedJSON.ResponseCode == "SUC"){
      counter++;
      if( counter >= 3 ) {
        enrollmentsDone();
      } else {
        startEnrollmentProcess(counter, enrollmentsDone);
      }
    }
  });
}

function runEnrollmentsAndAuthentication(){
      startEnrollmentProcess(1, ()=>{
        // Enrollment Done Do Authentication
        myVoiceIt.authentication({
        userId: 'developerUserId',
        password: 'd0CHipUXOk',
        pathToAuthenticationWav: '/home/users/username/authentication.wav',
        contentLanguage: 'en-US',
        callback:(response2)=>{
          var parsedJSON2 = JSON.parse(response2);
          if(parsedJSON2.ResponseCode == "SUC"){
            //SUCCESSFUL AUTHENTICATION
            console.log("SUCCESSFULLY AUTHENTICATED THE USER");
          } else {
            //UNSUCCESSFUL AUTHENTICATION
            console.log("USER FAILED AUTHENTICATION PLEASE TRY AGAIN!");
          }
        }
        });
      });
  }

myVoiceIt.getUser({
	userId: 'developerUserId',
	password: 'd0CHipUXOk',
	callback: (response)=>{
  var parsedJSON = JSON.parse(response);
  // User Exists so continuer with enrollment
  if(parsedJSON.ResponseCode == "SUC"){
      runEnrollmentsAndAuthentication();
  } else if (parsedJSON.ResponseCode == "UNF"){
       myVoiceIt.createUser({
      userId: 'developerUserId',
      password: 'd0CHipUXOk',
      callback: (response2)=>{
        var parsedJSON2 = JSON.parse(response2);
        if(parsedJSON2.ResponseCode == "SUC"){
          runEnrollmentsAndAuthentication();
        }
});
	}
});
