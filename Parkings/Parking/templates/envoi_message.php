<?php
if(isset($_POST['envoyer'])) {
    // Récupération des données du formulaire
    $nom = $_POST['nom'];
    $email = $_POST['email'];
    $sujet = $_POST['sujet'];
    $message = $_POST['message'];
    
    // Destinataire de l'e-mail
    $destinataire = "adresse-email-destinataire@example.com";
    
    // En-têtes de l'e-mail
    $headers = "From: $nom <$email>" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();
               
    // Envoi de l'e-mail
    if(mail($destinataire, $sujet, $message, $headers)) {
        echo "<p>Votre message a été envoyé avec succès !</p>";
    } else {
        echo "<p>Une erreur est survenue lors de l'envoi de votre message.</p>";
    }
}
?>
