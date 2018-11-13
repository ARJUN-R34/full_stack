function Read() {
  var name=document.getElementById("name").value;
  var roll=document.getElementById("roll").value;
  var admission=document.getElementById("adm_no").value;
  var age=document.getElementById("age").value;
  if(age<18) {
    alert("You are not eligible");
  }
  else {
    alert("You are eligible");
  }
}
