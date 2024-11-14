// On définit les différentes constantes pour les LEDs et le nombre maximum de tentatives
const int ledJaune = 5; 
const int ledRouge = 6;  
const int ledVerte = 4; 
const int maxTentatives = 10; 

// On définit les variables pour le nombre mystère, la proposition, le nombre de tentatives et l'état de traitement
int nombreMystere;       
int proposition;         
int nombreTentatives = 0; 
bool propositionTraitee = true; 

// On déclare les fonctions utilisées
void TropGrand();
void TropPetit();
void Gagne(bool tentativeReussie);

void setup() {
  // On configure les LEDs comme sorties
  pinMode(ledJaune, OUTPUT);
  pinMode(ledRouge, OUTPUT);
  pinMode(ledVerte, OUTPUT);

  // On initialise la communication série
  Serial.begin(9600);

  // On génère le nombre mystère aléatoire (entre 1 et 1024)
  randomSeed(analogRead(0));
  nombreMystere = random(1, 1025);
}

void loop() {
  // Si la proposition a été traitée, on fait clignoter la LED jaune en attente d'une nouvelle entrée
  if (propositionTraitee) {
    digitalWrite(ledJaune, HIGH);
    delay(500);
    digitalWrite(ledJaune, LOW);
    delay(500);
  }

  // On vérifie si une proposition a été envoyée via la communication série
  if (Serial.available() > 0) {
    //On lit la proposition et on la stocke dans la variable
    proposition = Serial.parseInt();
    propositionTraitee = false; // La proposition est maintenant en cours de traitement
    nombreTentatives++; // On incrémente le compteur de tentatives

    // On fait la comparaison de la proposition avec le nombre mystère
    if (proposition > nombreMystere) {
      TropGrand(); // On appelle la fonction TropGrand() si la proposition est trop élevée
      propositionTraitee = true; // On marque la proposition comme traitée
    } else if (proposition < nombreMystere) {
      TropPetit(); // On appelle la fonction TropPetit() si la proposition est trop basse
      propositionTraitee = true; // On marque la proposition comme traitée
    } else {
      // On vérifie si le joueur a réussi en moins de tentatives que le maximum
      bool tentativeReussie = (nombreTentatives <= maxTentatives); // Si oui, la variable prend la valeur true, sinon false
      Gagne(tentativeReussie); // On appelle la fonction Gagne()

      // On génère un nouveau nombre mystère pour recommencer le jeu
      nombreMystere = random(1, 1025);
      nombreTentatives = 0;  // On réinitialise le compteur de tentatives
      propositionTraitee = true; // On marque la proposition comme traitée
    }
  }
}

void TropGrand() {
  // On allume la LED rouge pour indiquer que la proposition est trop grande
  digitalWrite(ledRouge, HIGH);
  delay(1000); 
  digitalWrite(ledRouge, LOW);
}

void TropPetit() {
  // On allume la LED verte pour indiquer que la proposition est trop petite
  digitalWrite(ledVerte, HIGH);
  delay(1000); 
  digitalWrite(ledVerte, LOW); 
}

void Gagne(bool tentativeReussie) {
  // On allume la LED jaune pour indiquer que le joueur a gagné
  digitalWrite(ledJaune, HIGH);
  if (tentativeReussie) {
    // Si le joueur a réussi en moins de 10 tentatives, on allume la LED verte
    digitalWrite(ledVerte, HIGH);
  } else {
    // Sinon, on allume la LED rouge pour indiquer l'échec
    digitalWrite(ledRouge, HIGH);
  }
  delay(5000);
  digitalWrite(ledJaune, LOW);
  digitalWrite(ledVerte, LOW);
  digitalWrite(ledRouge, LOW);
}
