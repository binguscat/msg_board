function startTableFromServer() {
  // Instantiate an new XHR Object
  const xhr = new XMLHttpRequest();
  // Open an object (GET/POST, PATH, ASYN-TRUE/FALSE)
  // 2nd parameter is URL of API
  xhr.open("GET", "cgi-bin/loadTable.py", true);
  // When response is ready
  xhr.onload = function () {
    //If the response is returned successfully
    if (this.status === 200) {
      // Retrieve responseText and convert to JSON Object
      msg = JSON.parse(this.responseText);
      // Save a cookie with API info
      setCookie("messages",JSON.stringify(msg),365);
      startTable();
    }
    else {
      console.log("Invalid data");
    }
  }
  xhr.send();

}



function startTable(){
  var messages = getCookie('messages');
  messages = JSON.parse(messages);
  console.log(messages.data);
  var table = document.getElementById("messageTable");
  for(let i = 0; i < messages.length; i++)
  {
      var id = messages.i;
      var name = id.value[0];
      var msg = id.value[1];
      var time = id.value[2];
      var row = table.insertRow();

      //each cell
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      var cell3 = row.insertCell(2);
      var cell4 = row.insertCell(3);

      //create the elements
      var idNum = document.createElement('idNum');
      var  user = document.createElement('user');
      var msg = document.createElement('msg');
      var time = document.createElement('time');

      //user style
      user.innerHTML = price;
      user.style.fontSize = "x-large";

      cell1.appendChild(idNum);
      cell2.appendChild(user);
      cell3.appendChild(msg);
      cell4.appendChild(time);
    }
}



function getCookie(cname) {
 var name = cname + "=";
 var decodedCookie = decodeURIComponent(document.cookie);
 var ca = decodedCookie.split(';');
 for(var i = 0; i <ca.length; i++) {
   var c = ca[i];
   while (c.charAt(0) == ' ') {
     c = c.substring(1);
   }
   if (c.indexOf(name) == 0) {
     return c.substring(name.length, c.length);
   }
 }
 return null;
}



function setCookie(cname, cvalue, exdays) {
 var d = new Date();
 d.setTime(d.getTime() + (exdays*24*60*60*1000));
 var expires = "expires="+ d.toUTCString();
 document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
 alert(document.cookie);
}



function setUser(){
   var cname = "login";
   var user = document.getElementById("username");
   var user1 = user.value;
   var cvalue = JSON.stringify(user1);
   var exdays = 30;

   setCookie(cname, cvalue, exdays);

}

function logout(){
  document.cookie = "login=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
