<?php
if (!empty($_POST['cat'])) {
    $imageData = $_POST['cat'];
    $filtered = substr($imageData, strpos($imageData, ",") + 1);
    $decoded = base64_decode($filtered);
    file_put_contents("cam.png", $decoded);
}
?>
