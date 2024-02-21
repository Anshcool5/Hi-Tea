<!-- insert.php -->
<?php
// Connect to MySQL database
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Insert data into table
$name = $_POST["name"];
$email = $_POST["email"];
$number = $_POST["phone"];
$pc = $_POST["postalc"];
$id = 123;

$sql = "UPDATE users SET name='$name', email='$email', phone='$number', postalc='$pc' WHERE id = $id";

if ($conn->query($sql) === TRUE) {
  echo "Record updated successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>