<?php
  // Vérification des identifiants de connexion
  $username = $_POST['username'];
  $password = $_POST['password'];

  if ($username === 'monnomutilisateur' && $password === 'monmotdepasse') {
    // Connexion réussie, rediriger vers la page d'accueil
    header('Location: accueil.html');
    exit;
  } else {
    // Identifiants invalides, afficher un message d'erreur
    echo 'Identifiants invalides';
  }
?>
