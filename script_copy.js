document.querySelector('myForm').addEventListener('submit', function(event) {
    var name = document.getElementById('name').value;
    var postalCode = document.getElementById('postalCode').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    console.log(name);
    console.log(email);
    if (!name || !postalCode || !email || !phone) {
      alert('Please fill in all fields');
      event.preventDefault();
      return;
    }
  
    var data = {
      Name: name,
      Postal_Code: postalCode,
      Email: email,
      Phone_Num: phone
    };
  
    fetch('insert.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(function(response) {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(function(data) {
      console.log(data);
    })
    .catch(function(error) {
      console.error('There was a problem with the fetch operation:', error);
    });
  
    event.preventDefault();
  });