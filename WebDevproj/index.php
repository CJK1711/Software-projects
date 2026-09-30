<?php

while(!isset($_COOKIE["username"]) && !isset($_SESSION["username"])) {
    echo "You must be logged in to view products. <a href='login.php'>Login here</a>.";
    echo "<br><br>";
    echo '<a href="home.html">Home</a>';
    exit;
    
}

session_start();

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="pizza.png" type="image/x-icon">
    <link rel="stylesheet" href="adminstyle.css">
    <title>Menu admin</title>
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
        div.back {
            background-color: #ffffff;    
            margin-left: 10%;
            margin-right: 10%;
            padding: 20px;
            margin-bottom: 50px;
            margin-top: 50px;
        }
        div.back a :hover {
            text-decoration: underline;
            color: #0c39de;
            font-size: 16px;
            size : 18px;
        }
         body {
            background-color: #333;
                
            }
        body{
            
        }
        
        header {
            text-align: right;
            margin-top: 20px;
        }
        button {
            background-color: #000000;
            color: white;
            padding: 10px 20px;
            border: 2px solid #ff0000
            cursor: pointer;
            font-size: 20px;
            border-radius: 20px;
            border-color: #ff0000;
        }
        button:hover {
            background-color: #1a08a2;
            
        }
    </style>
</head>
<body>



<header>
    <form action="" method="post">
<button type="submit" name="Logout">Logout</button>
</form>
<center><h1>Welcome, <?php echo $_SESSION["username"]; ?>!</h1></center>



</header>
<div class="back">
<?php
if (isset($_POST["Logout"])) {
    setcookie("username", "admin", time() - (3600), "/");
    unset($_COOKIE["username"]);
    session_abort();
    echo "logged out <a href='login.php'>Login here</a>.";
    echo "<br><br>";
    echo '<a href="home.html">Home</a>';
    exit;
}
    

?>

<center><h1>Menu Admin</h1>
<?php
if (isset($_COOKIE["username"])) {

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "project";
$conn = new mysqli($servername, $username, $password, $dbname);
$sql = "SELECT ProductID, PName, Description, Price FROM starter";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo"<h1>Starters</h1>";
    echo "<table border='1'>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>";
        echo(htmlentities($row["ProductID"]));
        echo "</td><td>";
        echo(htmlentities($row["PName"]));
        echo("</td><td>");
        echo(htmlentities($row["Description"]));
        echo("</td><td>");
        echo(htmlentities($row["Price"]));
        echo("</td><td>\n");
        echo('<a href="editstarter.php?id='.htmlentities($row["ProductID"]).'">Edit</a> / ');
        echo('<a href="deletestarter.php?id='.htmlentities($row["ProductID"]).'">Delete</a>');
        echo("</td></tr>\n");
        
    }
    echo"</table>";
    echo '<a href="addstarter.php">Add New Starter</a>';
    echo "<br><br>";
} else {
    echo"<h1>Starters</h1>";
    echo "0 results";
    echo '<a href="addstarter.php">Add New Starter</a>';
    echo "<br><br>";
}


$sql = "SELECT ProductID, PName, Description, Price FROM product";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo "<h1>Pizzas</h1>";
    echo "<table border='1'>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>";
        echo(htmlentities($row["ProductID"]));
        echo "</td><td>";
        echo(htmlentities($row["PName"]));
        echo("</td><td>");
        echo(htmlentities($row["Description"]));
        echo("</td><td>");
        echo(htmlentities($row["Price"]));
        echo("</td><td>\n");
        echo('<a href="edit.php?id='.htmlentities($row["ProductID"]).'">Edit</a> / ');
        echo('<a href="delete.php?id='.htmlentities($row["ProductID"]).'">Delete</a>');
        echo("</td></tr>\n");
        
    }
    echo"</table>";
    echo '<a href="add.php">Add New Pizza</a>';
    echo "<br><br>";
} else {
    echo "<h1>Pizzas</h1>";
    echo "0 results";
    echo '<a href="add.php">Add New Pizza</a>';
    echo "<br><br>";
}




$sql = "SELECT ProductID, PName, Description, Price FROM dessert";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo "<h1>Desserts</h1>";
    echo "<table border='1'>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>";
        echo(htmlentities($row["ProductID"]));
        echo "</td><td>";
        echo(htmlentities($row["PName"]));
        echo("</td><td>");
        echo(htmlentities($row["Description"]));
        echo("</td><td>");
        echo(htmlentities($row["Price"]));
        echo("</td><td>\n");
        echo('<a href="editdessert.php?id='.htmlentities($row["ProductID"]).'">Edit</a> / ');
        echo('<a href="deletedessert.php?id='.htmlentities($row["ProductID"]).'">Delete</a>');
        echo("</td></tr>\n");
        
    }
    echo"</table>";
    echo '<a href="adddessert.php">Add New Dessert</a>';
} else {
    echo"<h1>Desserts</h1>";
    echo "0 results";
    echo '<a href="adddessert.php">Add New Dessert</a>';
}
$conn->close();
}
else 
    echo "You must be logged in to view products. <a href='login.php'>Login here</a>.";
    exit;
?>

<br>
</center>
<footer>

</footer>
</div>
</body>
</html>