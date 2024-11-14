FR : PROJET CODÉ PAR ANTHONY VAUCHEL

PROJET SCOLAIRE

L'objectif de ce projet était de développer un jeu de "nombre mystère" basé sur la communication Bluetooth avec une carte Arduino Uno. Dans ce jeu, l'Arduino génère un nombre aléatoire, et le joueur doit essayer de deviner ce nombre en envoyant des propositions depuis une application sur smartphone (j'ai personnellement utilisé Arduino Bluetooth Controller pour cela).

Pour ce projet, plusieurs éléments ont été réalisés :

-Un montage électrique comporta,t trois LEDs (une rouge, une verte et une jaune) et le module Bluetooth HC-06, utilisés pour communiquer et donner un feedback visuel. On peut retrouver ce montage dans les photos jointes.
-Des fonctions comme TropGrand() et TropPetit() ont été créées pour comparer chaque proposition envoyée par l'utilisateur avec le nombre mystère. Si la proposition est trop élevée, trop basse ou alors égale au nombre mystère, l'Arduino renvoie un retour visuel avec les LEDs.
-Un feedback visuel : La LED rouge s’allume si la proposition est trop élevée, la LED verte s’allume si la proposition est trop basse, la LED jaune s’allume pour signaler une victoire lorsque le nombre mystère est deviné. Si le joueur trouve le nombre en moins de 10 tentatives, cela est également indiqué par les LEDs.

Ce projet m'a permis de comprendre plusieurs choses :

-La mise en place du circuit m'a permis de me familiariser avec les composants électroniques de base (LEDs, module Bluetooth, résistances) et leur utilisation avec une carte Arduino.
-J'ai découvert comment échanger des données entre un smartphone et l'Arduino via le module HC-06.
-En utilisant des fonctions de comparaison, j'ai pu consolider mes connaissances existantes.
	

EN : PROJECT CODED BY ANTHONY VAUCHEL

SCHOOL PROJECT


The objective of this project was to develop a "mystery number" game based on Bluetooth communication with an Arduino Uno board. In this game, the Arduino generates a random number, and the player must try to guess this number by sending guesses from a smartphone application (I personally used Arduino Bluetooth Controller for this).

For this project, several elements were implemented:

-An electrical setup with three LEDs (a red, a green, and a yellow one) and the HC-06 Bluetooth module, used to communicate and provide visual feedback. This setup can be seen in the attached photos.
-Functions like TropGrand() and TropPetit() were created to compare each guess sent by the user with the mystery number. If the guess is too high, too low, or equal to the mystery number, the Arduino provides visual feedback with the LEDs.
-Visual feedback: The red LED lights up if the guess is too high, the green LED lights up if the guess is too low, and the yellow LED lights up to signal a win when the mystery number is guessed. If the player guesses the number in fewer than 10 attempts, this is also indicated by the LEDs.

This project allowed me to understand several things:

-Setting up the circuit helped me become familiar with basic electronic components (LEDs, Bluetooth module, resistors) and their use with an Arduino board.
-I learned how to exchange data between a smartphone and the Arduino via the HC-06 module.
-By using comparison functions, I was able to consolidate my existing knowledge.
