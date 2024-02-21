<?php
$data = $_POST;
$json = json_encode($data);
$file = "data.json";
if (file_put_contents($file, $json, FILE_APPEND | LOCK_EX) === false) {
  echo 'Error writing to file';
} else {
  echo 'Data written to file';
}
?>