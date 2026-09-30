

<!Doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="pizza.png" type="image/x-icon">
    <style>

        body {
            background-color: #333;
                
            }
        div.back {
            background-color: #ffffff;    
            margin-left: 10%;
            margin-right: 10%;
            padding: 20px;
        }

        h1 {
            text-align: center;
            font-size: 40px;
            text-decoration: underline;
        }
        p {
            text-align: center;
            font-size: 14px;
        }
        h2 {
            text-align: center;
            font-size: 18px;
        }
        h3 {
            text-align: center;
            font-size: 16px;
        }
        footer {
            margin-top: 50px;
            border: 5px solid #000000;
            padding: 20px;
            margin-left: 20%;
            margin-right: 20%;
        }

        div.content {
            margin-top: 50px;
        }

        div.content a{
            text-align: center;
            text-decoration: underline;
            color: #000000;
            font-size: 20px;
        }

        div.content a:hover {
            font-size: 22px;
            color: #008cff;
        }

    </style>
</head>
<body>
    <div class="sideleft">
        </div>
        <div class="sideright">
        </div>
<header>
    <a href="home.html">Home</a>
    <a href="menu.php" style="background-color: #a20808; color: white; padding: 10px; text-decoration: underline; font-size: 40px;">Menu</a>
    <a href="login.php">Login</a>
</header>
<div class="back">
<div class="content">
<center>
<a href="starter.php">Starters</a>
<a href="menu.php">Pizza</a>
</center>
</div>

<footer>
    <h1>Desserts</h1>
    <br>
    
<?php


$servername = "localhost";
$username = "root";
$password = "";
$dbname = "project";
$conn = new mysqli($servername, $username, $password, $dbname);
$sql = "SELECT PName, Description, Price FROM dessert";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    
    while($row = $result->fetch_assoc()) {
        
        echo("<hr>");
        echo("<h2>" . htmlentities($row["PName"]) . "</h2>");
        
        echo("<h3> Description: </h3>");
        echo("<p>" . htmlentities($row["Description"]) . "</p>");
        echo("<br>");
        
        echo("<h3>Price: €" . htmlentities($row["Price"]) . "</h3>");
        echo("<br>");
        
        
    }
    
}

?>
</footer>
</div>
</body>
</html>
