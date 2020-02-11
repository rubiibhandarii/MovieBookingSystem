$(document).ready(()=>{
    $("#csearch").keyup(()=>{
      $.ajax({
        data:{search:$("#csearch").val()},
        url:'/dashboard/customer/search',
        method:'GET',
        success:function(data){
           console.log(data)
           $("tr").not("tr.first").remove();
           var html="";
           for(d of data){
              html+="<tr>";
                html+="<td>"+d.c_id+"</td>";
                html+="<td>"+d.c_first_name+"</td>";
                html+="<td>"+d.c_last_name+"</td>";
                html+="<td>"+d.c_email+"</td>";
                html+="<td>"+d.c_password+"</td>";
                html+="<td><a href='/dashboard/customer/edit/"+d.c_id+"'>Edit</a>|<a href='/dashboard/customer/delete/"+d.c_id+"'>Delete</a></td>";
              html+="</tr>";

              $("table").append(html);
           }
        },error:function(data){
          console.log(error)
        },complete:function(){
          console.log("completed");
        }
      })
    })



    $("#usersearch").keyup(()=>{
      $.ajax({
        data:{search:$("#usersearch").val()},
        url:'/dashboard/usertable/search',
        method:'GET',
        success:function(data){
           console.log(data)
           $("tr").not("tr.first").remove();
           var html="";
           for(d of data){
              html+="<tr>";
                html+="<td>"+d.u_id+"</td>";
                html+="<td>"+d.u_email+"</td>";
                html+="<td>"+d.u_password+"</td>";
                html+="<td><a href='/dashboard/usertable/edit/"+d.u_id+"'>Edit</a>|<a href='/dashboard/usertable/delete/"+d.u_id+"'>Delete</a></td>";
              html+="</tr>";

              $("table").append(html);
           }
        },error:function(data){
          console.log(error)
        },complete:function(){
          console.log("completed");
        }
      })
    })



  $("#upassword").keyup(()=>{
    if ($("upassword").val().length>5){
      alert("greater than 5")
      $("#usersubmit").prop("disabled",true)
    }
  })
})
})
