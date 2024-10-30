<h1> Python Project 11: Blackjack Game </h1>
<p><em>Updated 29 October 2024: Reattempted capstone project and committed new changes to practice what I've learned. I found that the second attempt was somewhat easier as I had a better grasp of what was needed to write this code; however, I did still get stuck in some places as I had some elements in the wrong order or incorrectly indented, which I was able to fix up upon review. This is a project that I would like to re-write and practice again in the future.</em></p>
<h2>Summary</h2>
<p>This project is for day 11 of the 100 Days of Code challenge that I'm completing as part of the Complete Python Pro Bootcamp with Dr. Angela Yu from the London App Brewery. Each project in this challenge will be using Python so that I can grow my skills in software development.</p>
<p>This project is a simple game of Blackjack with the following "house rules":
<ul>
  <li>
    The deck is unlimited in size.
  </li>
  <li>
    There are no jokers.
  </li>
  <li>
    The Jack/Queen/King count as 10 each.
  </li>
  <li>
    Ace counts as 11 or 1.
  </li>
  <li>
    Cards have equal probability of being drawn.
  </li>
  <li>
    Cards are not removed from the deck as they are drawn.
  </li>
  <li>
    The computer is the dealer.
  </li>
</ul></p>
<p>
  In this game, two cards each are randomly selected from the card list for the user and the computer; however, only 1 of the cards for the computer is revealed until the user has finished drawing more cards. The goal of Blackjack is to get a score of 21. If either card hand goes over 21, they lose. If neither hand gets 21 or goes over 21, the highest score wins. At the end of each game, the user will be asked if they want to keep playing, and a new game will occur as long as the user wishes to play.
</p>
<h3>Learnings</h3>
<ul>
  <li>
    This project allowed me to combine all of the Python skills learned so far in the course, including choice(), remove(), append() functions; defining functions; if/elif/else statements; for and while loops; and accessing list values. I found I mostly remembered how to write these Python codes, but I did need to research a few of them to ensure I had the inputs correctly added in. For example, I initially had the for loop with a range using two digits "(0, 2)" rather than just "(2)". This was easily fixed upon reviewing for range documentation online.
  </li>
  <li>
    During the solution video, I also learned that adding "computer_score = -1" and "user_score = -1" when defining the standard variables helped debug the second while loop on line 69, as it meant that the second loop would still work correctly if something happened to stop the first while loop on line 53 from running beforehand.
  </li>
</ul>
<h2>Tech stack</h2>
<ul>
  <li>Python</li>
  <li>VS Code</li>
  <li>PyCharm</li>
  <li>ASCII</li>
