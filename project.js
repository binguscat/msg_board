
var messages = {};

function startTableFromServer() {
  // Instantiate an new XHR Object
  const xhr = new XMLHttpRequest();
  // Open an object (GET/POST, PATH, ASYN-TRUE/FALSE)
  // 2nd parameter is URL of API
  xhr.open("GET", "cgi-bin/readMsg.py", true);
  // When response is ready
  xhr.onload = function () {
    //If the response is returned successfully
    if (this.status === 200) {
      // Retrieve responseText and convert to JSON Object
      messages = JSON.parse(this.responseText);
      // Save a cookie with API info
      setCookie("messages",JSON.stringify(messages),365);
      startTable();
    }
    else {
      console.log("Invalid data");
    }
  }
  xhr.send();

}



function startTable(){
  console.log(messages);
  var table = document.getElementById("messageTable");
  for (const i in messages)
  {
     console.log("IN FOR LOOP");
      // var id = messages.i;
      // var name = id.value[2];
      // var msg = id.value[1];
      // var time = id.value[3];
      // var row = table.insertRow();
      var id = messages[i]["id"];
      console.log(id);
      var name = messages[i]["username"];
      console.log(name);
      var msg = messages[i]["message"];
      console.log(msg);
      var time = messages[i]["time"];
      console.log(time);

      var row = document.createElement("tr");

      var idCol = document.createElement("td");
      var nameCol = document.createElement("td");
      var msgCol = document.createElement("td");
      var timeCol = document.createElement("td");

      idCol.innerHTML = id;
      nameCol.innerHTML = name;
      msgCol.innerHTML = msg;
      timeCol.innerHTML = time;

      row.appendChild(idCol);
      row.appendChild(nameCol);
      row.appendChild(msgCol);
      row.appendChild(timeCol);

      table.appendChild(row);

      // //each cell
      // var cell1 = row.insertCell(0);
      // var cell2 = row.insertCell(1);
      // var cell3 = row.insertCell(2);
      // var cell4 = row.insertCell(3);
      //
      // //create the elements
      // var idNum = document.createElement('idNum');
      // var user = document.createElement('user');
      // var msg = document.createElement('msg');
      // var time = document.createElement('time');

      //user style
      // user.innerHTML = price;
      // user.style.fontSize = "x-large";

      // cell1.appendChild(idNum);
      // cell2.appendChild(user);
      // cell3.appendChild(msg);
      // cell4.appendChild(time);
    }
}



// function getCookie(cname) {
//  var name = cname + "=";
//  var decodedCookie = decodeURIComponent(document.cookie);
//  var ca = decodedCookie.split(';');
//  for(var i = 0; i <ca.length; i++) {
//    var c = ca[i];
//    while (c.charAt(0) == ' ') {
//      c = c.substring(1);
//    }
//    if (c.indexOf(name) == 0) {
//      return c.substring(name.length, c.length);
//    }
//  }
//  return null;
// }



function setCookie(cname, cvalue, exdays) {
 var d = new Date();
 d.setTime(d.getTime() + (exdays*24*60*60*1000));
 var expires = "expires="+ d.toUTCString();
 document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
 alert(document.cookie);
 console.log("SET COOKIE");
}



function setUser(){
   var cname = "login";
   var user = document.getElementById("username");
   var user1 = user.value;
   var cvalue = JSON.stringify(user1);
   var exdays = 30;

   setCookie(cname, cvalue, exdays);
}

function setCAP(){
   var cname = "CAP";
   var user = document.getElementById("userNum");
   var user1 = user.value;
   var cvalue = JSON.stringify(user1);
   var exdays = 30;

   setCookie(cname, cvalue, exdays);
}

function logout(){
  document.cookie = "login=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}
