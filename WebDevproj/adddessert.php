<?php
if (!isset($_COOKIE["username"])) {
    echo "You must be logged in to edit products. <a href='login.php'>Login here</a>.";
    echo "<br><br>";
    echo '<a href="home.html">Home</a>';
    exit;

}
else {
    session_start();
}

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add</title>
    
    <link rel="icon" href="pizza.png" type="image/x-icon">
    <link rel="stylesheet" href="adminstyle.css">
    <style>
        a{
            text-decoration: none;
            color: #0c39de;
            font-size: 17px;
        }
        a :hover {
            text-decoration: underline;
            color: #0c39de;
            font-size: 17px;
        }
         body {
            background-color: #333;
                
            }
        div.back {
            background-color: #ffffff;
            margin-left: 10%;
            margin-right: 10%;
            padding: 20px;
            margin-bottom: 50px;
            margin-top: 50px;
        }

    </style>
</head>

<body>
    <header>
    
    <center><h1>Logged in as <?php echo $_SESSION["username"]; ?></h1></center>
</header>
<div class="back">
<?php
if (isset($_COOKIE["username"])) {
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "project";
$conn = new mysqli($servername, $username, $password, $dbname);
if (isset($_POST['PName']) && isset($_POST['Description']) && isset($_POST['Price'])) 
{ 
$n = $conn -> real_escape_string($_POST['PName']); 
$d = $conn -> real_escape_string($_POST['Description']);
$p = $conn -> real_escape_string($_POST['Price']);
$sql = "INSERT INTO dessert (PName, Description, Price) VALUES ('$n', '$d', '$p')";
echo "<pre>\n$sql\n</pre>\n";
$conn->query($sql);
echo 'Success <a href="index.php">Continue...</a>'; 
return; 
}
} else {
    echo "You must be logged in to add products. <a href='login.php'>Login here</a>.";
    exit;
}
?> 
<center>
<p>Add A New Dessert</p> 
<form method="post">
    <p>Name: <input type="text" name="PName"></p> 
    <p>Description: <input type="text" name="Description"></p>
    <p>Price: <input type="number" name="Price" step="0.01" min="0"></p>
    <p><input type="submit" value="Add New"/>
    <a href="index.php">Cancel</a></p>
</form>
</center>
</div>
</body>
</html>