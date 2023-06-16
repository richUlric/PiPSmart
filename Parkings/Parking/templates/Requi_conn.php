<?php
// Inclusion du fichier de configuration de la base de données
require_once "config.php";

// Vérification de la connexion à la base de données
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("La connexion a échoué : " . mysqli_connect_error());
}

// Requête SQL pour récupérer la liste des places de parking disponibles
$sql = "SELECT * FROM places_de_parking WHERE disponible=1";

$result = mysqli_query($conn, $sql);

// Affichage de la liste des places de parking disponibles
if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
        echo "Place de parking #" . $row["id"] . " - Emplacement: " . $row["emplacement"] . "<br>";
    }
} else {
    echo "Il n'y a aucune place de parking disponible pour le moment.";
}

// Fermeture de la connexion
mysqli_close($conn);
?>
