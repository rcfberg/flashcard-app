// Words data (German: English)
const words = [
    { german: "Hallo", english: "Hello" },
    { german: "Danke", english: "Thank you" },
    { german: "Bitte", english: "Please / You're welcome" },
    { german: "Guten Morgen", english: "Good morning" },
    { german: "Guten Abend", english: "Good evening" },
    { german: "Ja", english: "Yes" },
    { german: "Nein", english: "No" },
    { german: "Ich heiße", english: "My name is" },
    { german: "Wie geht es Ihnen?", english: "How are you? (formal)" },
    { german: "Gut", english: "Good" }
];

let currentWordIndex = 0;
let isFlipped = false;

// DOM Elements
const germanWordElement = document.getElementById('german-word');
const englishTranslationElement = document.getElementById('english-translation');
const flashcardElement = document.querySelector('.flashcard'); // Corrected selector
const flipButton = document.getElementById('flip-button');
const nextButton = document.getElementById('next-button');

// Function to display a word
function displayWord() {
    germanWordElement.textContent = words[currentWordIndex].german;
    englishTranslationElement.textContent = words[currentWordIndex].english;
    if (isFlipped) {
        // If card was flipped, unflip it for the new word
        flashcardElement.classList.remove('flipped');
        isFlipped = false;
    }
}

// Function to flip the card
function flipCard() {
    flashcardElement.classList.toggle('flipped');
    isFlipped = !isFlipped;
}

// Function to go to the next word
function nextWord() {
    currentWordIndex++;
    if (currentWordIndex >= words.length) {
        currentWordIndex = 0; // Loop back to the first word
    }
    displayWord();
}

// Event Listeners
flipButton.addEventListener('click', flipCard);
nextButton.addEventListener('click', nextWord);
// Allow flipping by clicking the card itself
flashcardElement.addEventListener('click', flipCard);


// Initial display
displayWord();
