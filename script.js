var name = document.getElementById('name').value;
var postalCode = document.getElementById('postalCode').value;
var email = document.getElementById('email').value;
var phone = document.getElementById('phone').value;
var subBtn = document.getElementById("sub");
var subText = document.getElementById("jsonText");

subBtn.addEventListener("click", function(){
  var data = {
    Name: name,
    Postal_Code: postalCode,
    Email: email,
    Phone_Num: phone
  };
  subText.innerHTML = JSON.stringify(data);
  console.log(data)
});

  