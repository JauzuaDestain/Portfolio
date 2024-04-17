// Sélectionne l'élément img de cv-div
const cvImage = document.querySelector('.cv-container > .arrow-show');

// Sélectionne l'élément PDF
const pdfElement = document.querySelector('.pdf1');

// Ajoute un écouteur d'événements au clic sur l'image de cv-div
cvImage.addEventListener('click', function() {
  // Vérifie si l'élément PDF est déjà visible
  if (pdfElement.classList.contains('visible')) {
    // Si oui, retire la classe 'visible' pour le cacher
    pdfElement.classList.remove('visible');
  } else {
    // Sinon, ajoute la classe 'visible' pour le montrer
    pdfElement.classList.add('visible');
  }
});

const motivImage = document.querySelector('.motiv-container > .arrow-show');
// Sélectionne l'élément PDF
const pdfElement2 = document.querySelector('.pdf2');

motivImage.addEventListener('click', function() {
  // Vérifie si l'élément PDF est déjà visible
  if (pdfElement2.classList.contains('visible')) {
    // Si oui, retire la classe 'visible' pour le cacher
    pdfElement2.classList.remove('visible');
  } else {
    // Sinon, ajoute la classe 'visible' pour le montrer
    pdfElement2.classList.add('visible');
  }
});
// Sélectionne le bouton .btn-play
const btnPlay = document.querySelector('.btn-play');

// Sélectionne le <li> de la classe .hero-content
const heroContentLi = document.querySelector('.txt > li');

// Ajoute un écouteur d'événements au clic sur le bouton .btn-play
btnPlay.addEventListener('click', function() {
  // Vérifie si le <li> de la classe .hero-content est déjà visible
  if (heroContentLi.style.display === 'block') {
    // Si oui, le cache en le rendant invisible
    heroContentLi.style.display = 'none';
    heroContentLi.style.opacity = '0';
    btnPlay.textContent = 'Commencer la présentation';
  } else {
    // Sinon, l'affiche en le rendant visible
    heroContentLi.style.display = 'block';
    heroContentLi.style.opacity = '1';
    btnPlay.textContent = 'Terminer la présentation';
    heroContentLi.style.transition = '4s';
  }
});

const Proj = document.querySelector('.exp-proj-container > .arrow-show');

// Sélectionne l'élément PDF
const Element = document.querySelector('.projets');

// Ajoute un écouteur d'événements au clic sur l'image de cv-div
Proj.addEventListener('click', function() {
  // Vérifie si l'élément PDF est déjà visible
  if (Element.classList.contains('visible')) {
    // Si oui, retire la classe 'visible' pour le cacher
    Element.classList.remove('visible');
  } else {
    // Sinon, ajoute la classe 'visible' pour le montrer
    Element.classList.add('visible');
  }
});