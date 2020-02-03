function validateUser(){
  var email = document.getElementById('id_c_email').value;
  var password=document.getElementById('id_c_password').value;
  var lname=document.getElementById('id_c_last_name').value;


  if (!isNaN(lname)){
      document.getElementById('spanlname').innerHTML="*Only characters are allowed";
      return false;
    }

  if(email.indexOf('@')<=1){
    document.getElementById('spanemail').innerHTML="*invalid '@' position";
    return false;
  }

  if(password.length < 8){
      document.getElementById('spanpswrd').innerHTML="*Please enter more than 8 characters";
      return false;
  }
  alert("New customer is added successfully !")

}
