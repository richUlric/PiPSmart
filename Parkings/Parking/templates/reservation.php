<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $to = 'adresse_email_destinataire@example.com';
    $subject = 'Nouvelle réservation';
    $message = "Nom: " . $_POST['nom'] . "\r\n" .
               "E-mail: " . $_POST['email'] . "\r\n" .
               "Date: " . $_POST['date'] . "\r\n" .
               "Heure: " . $_POST['heure'] . "\r\n";
    $headers = 'From: adresse_email_emetteur@example.com' . "\r\n" .
               'Reply-To: adresse_email_emetteur@example.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    mail($to, $subject, $message, $headers);
}
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Réservation</title>
  </head>
  <body>
    <h1>Réservation</h1>
    <form action="reservation.php" method="POST">
      <label for="nom">Nom :</label>
      <input type="text" id="nom" name="nom" required><br><br>
      <label for="email">E-mail :</label>
      <input type="email" id="email" name="email" required><br><br>
      <label for="date">Date :</label>
      <input type="date" id="date" name="date" required><br><br>
      <label for="heure">Heure :</label>
      <input type="time" id="heure" name="heure" required><br><br>
      <input type="submit" value="Réserver">
    </form>
  </body>
</html>