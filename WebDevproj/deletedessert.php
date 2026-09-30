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
    <title>Delete</title>
    
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
<center>
<?php
if (isset($_COOKIE["username"])) {
    // User is logged in, proceed with the delete operation
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "project";
$conn = new mysqli($servername, $username, $password, $dbname);
if ( isset($_POST['delete']) && isset($_POST['id']) ) {
$id = $conn -> real_escape_string($_POST['id']);
$sql = "DELETE FROM dessert WHERE ProductID = $id";
echo "<pre>\n$sql\n</pre>\n";
$conn->query($sql);
echo 'Success - <a href="index.php">Continue...</a>';
return;
}
$id = $conn -> real_escape_string($_GET['id']);
$sql = "SELECT PName,ProductID FROM dessert WHERE ProductID='$id'";
$result = $conn ->query($sql);
$row = $result->fetch_assoc();
echo "<p>Confirm: Deleting ". $row["PName"] . "</p>\n";
echo('<form method="post"><input type="hidden" ');
echo('name="id" value="'.htmlentities($row["ProductID"]).'">'."\n");
echo('<input type="submit" value="Delete" name="delete">');
echo('<a href="index.php">Cancel</a>');
echo("\n</form>\n");
} else {
    echo "You must be logged in to delete products. <a href='login.php'>Login here</a>.";
    exit;
}
?>
</center>
</div>
</body>
</html>