<?php
// Étape 2 : Traitement des données du formulaire d'inscription

// Récupérer les données du formulaire d'inscription
$nom = $_POST['nom'];
$prenom = $_POST['prenom'];
$mot_de_passe = $_POST['mot_de_passe'];

// Étape 3 : Connexion à la base de données

// Paramètres de connexion à la base de données
$host = 'localhost'; // Adresse de l'hôte de la base de données
$utilisateur = 'ulrich'; // Nom d'utilisateur de la base de données
$mot_de_passe_db = 'U1RICH@'; // Mot de passe de la base de données
$nom_db = 'parking'; // Nom de la base de données

// Établir la connexion à la base de données
$connexion = mysqli_connect($host, $utilisateur, $mot_de_passe_db, $nom_db);

// Vérifier si la connexion a échoué
if (!$connexion) {
    die("Échec de la connexion à la base de données : " . mysqli_connect_error());
}

// Étape 4 : Exécution de la requête d'insertion

// Requête d'insertion SQL
// Requête d'insertion SQL avec des paramètres
$requete = "INSERT INTO individus (nom, prenom, email, mot_de_passe) VALUES (?, ?, ?, ?)";

// Préparation de la requête
$statement = mysqli_prepare($connexion, $requete);

// Vérification de la préparation de la requête
if ($statement) {
    // Liaison des paramètres
    mysqli_stmt_bind_param($statement, "ssss", $nom, $prenom, $email, $mot_de_passe);

    // Exécution de la requête préparée
    if (mysqli_stmt_execute($statement)) {
        echo "L'inscription a été effectuée avec succès !";
    } else {
        echo "Erreur lors de l'inscription : " . mysqli_stmt_error($statement);
    }

    // Fermeture du statement
    mysqli_stmt_close($statement);
} else {
    echo "Erreur lors de la préparation de la requête : " . mysqli_error($connexion);
}

?>

