function validateCustomerEdit(){

  var firstname=document.getElementById('customerfirstnameedit').value;
  var lastname=document.getElementById('customerlastnameedit').value;
  var email = document.getElementById('customeremailedit').value;

  if (!isNaN(firstname)){
    document.getElementById('spancustomerfirstnameedit').innerHTML="**Only characters are allowed";
    return false;
  }
    if (!isNaN(lastname)){
      document.getElementById('spancustomerlastnameedit').innerHTML="**Only characters are allowed";
      return false;
    }

    if(email.indexOf('@')<=0){
      document.getElementById('spancustomeremailedit').innerHTML="**invalid '@' position";
      return false;
    }
    alert("Edited successfully !")
}



function validateUserEdit(){
  var email = document.getElementById('useremailedit').value;
  var password = document.getElementById('userpasswordedit').value;
    if(email.indexOf('@')<=0){
      document.getElementById('spanuseremailedit').innerHTML="**invalid '@' position";
      return false;
    }

    if(password.length<8){
      document.getElementById('spanuserpasswordedit').innerHTML="**Please enter more than 8 characters";
      return false;
    }
    alert("Edited successfully !")
}


function validateTicketEdit(){
  var email=document.getElementById('ticketemailedit').value;
   if(email.indexOf('@')<=0){
     document.getElementById('spanticketemailedit').innerHTML="**invalid '@' position";
     return false;
   }
   if((email.charAt(a.length-4)!='.') && (email.charAt(a.length-3)!='.')) {
     document.getElementById('spanticketemailedit').innerHTML="**invalid '.' position";
     return false;
   }
    alert("Edited successfully !")
}


function validateMovieEdit(){
  var match=document.getElementById('matchnameedit').value;
  if (!isNaN(match)){
  document.getElementById('spanmatchname').innerHTML="**Only characters are allowed";
  return false;
}
    alert("Edited successfully !");
}

function validateMovie(){
  var movie=document.getElementById('id_m_movie_name').value;
  if (!isNaN(movie)){
  document.getElementById('spanmatchname1').innerHTML="**Only characters are allowed";
  return false;
}
    alert("Movies created successfully !");
}

function validateUserDash(){
  var email = document.getElementById('id_u_email').value;
  var password = document.getElementById('id_u_password').value;
    if(email.indexOf('@')<=0){
      document.getElementById('spanuseremaildash').innerHTML="**invalid '@' position";
      return false;
    }

    if(password.length<8){
      document.getElementById('spanuserpassworddash').innerHTML="**Please enter more than 8 characters";
      return false;
    }
    alert("User added successfully !")
}
