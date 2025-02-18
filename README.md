<h1>Hangman</h1>

<h2>Languages and Utilities Used</h2>
<ul>
  <li>Python for game logic and functionality</li>
  <li>Console-based UI for text-based gameplay</li>
  <li>NLTK (Natural Language Toolkit) for selecting words from the English corpus</li>
</ul>

<h2>Description</h2>
Hangman is a text-based console game where players try to guess a randomly selected word before running out of attempts. The game includes difficulty levels (easy, medium, and hard) and provides an interactive experience with visual feedback through ASCII art for each incorrect guess. The objective is to guess the word by suggesting letters or the entire word, while avoiding mistakes that would lead to the completion of the hangman figure. The game ends when the player guesses the word correctly or exhausts their allowed attempts.
<br />

<h3>Difficulty Settings</h3>
<p>The game allows the player to select the difficulty level, which impacts the length of the words chosen for guessing:</p>
<ul>
  <li><b>Easy:</b> Words with 4 or fewer letters.</li>
  <li><b>Medium:</b> Words with 5 to 7 letters.</li>
  <li><b>Hard:</b> Words with 8 or more letters.</li>
</ul>

<p align="center">
ASCII Art Hangman: <br/>
<img src="https://i.imgur.com/tV1WLQp.png" height="20%" width="20%" alt="ASCII Art Hangman"/>
<br />
<br />

<h2>NLTK Implementation</h2>
<h3>Word Selection with NLTK</h3>
<p>The game uses the NLTK (Natural Language Toolkit) library to select words randomly from the English corpus. The NLTK library is a powerful suite of text processing libraries that allows for easy manipulation of language data. It includes several corpora (collections of words) that can be used for various language processing tasks.</p>
<p>In this game, we specifically use the 'words' corpus, which contains a large collection of English words. The game accesses this corpus to randomly choose words for the player to guess based on the selected difficulty level.</p>

<p>Before using the 'words' corpus, the code checks if it has already been downloaded using a `try-except` block. If the corpus is not found, it automatically downloads the required word list.</p>

