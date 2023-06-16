<?php
// Inclusion du fichier de configuration de la base de données
require_once "config.php";

// Vérification de la connexion à la base de données
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
    die("La connexion a échoué : " . mysqli_connect_error());
}

// Récupération des données du formulaire
$identifiant = $_POST["identifiant"];
$mot_de_passe = $_POST["mot_de_passe"];

// Requête SQL pour vérifier les données dans la table "utilisateurs"
$sql = "SELECT * FROM utilisateurs WHERE identifiant='$identifiant' AND mot_de_passe='$mot_de_passe'";

$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) == 1) {
    echo "Les informations d'identification sont correctes.";
} else {
    echo "Les informations d'identification sont incorrectes.";
}

// Fermeture de la connexion
mysqli_close($conn);
?>
