# RockPaperScissorsPredictingModel
simple program which can predict your future moves

# 🤖 Rock Paper Scissors - AI Move Predictor

> Game of rockk paper scissors with a learning opponent, who learns from your moves, the move you play with it, the move it will learn and get better than you.

---
# One of the application

## ⚽ The Sports Analytics Connection

Why start with Rock-Paper-Scissors?

I wanted to showcase the technology used in predicting stats and performance of playeers and games of real life sports.

This project will help us understand what all different types of models are used to predict.

A game of rock-paper-scissors is universally understood and need no explanation. It is also a defination of random moves. 

But at a certain point if you just zoom out at a great scale you will find a pattern, it is not truly random, if we are able to giev the correct amount/quantity of data we might be able to guess/predict the future move.

This might apply in many fields not only in sports.



Humans are notoriously bad at generating true randomness. When a player makes a move, they leave behind psychological patterns (e.g., *"If I lose with Rock, I am 60% more likely to switch to Paper"*). 

This repository uses **1st-Order Markov Chains** (Transition Probabilities) to track decision patterns. In real-world sports, this exact mathematical principle is used to:

* **Baseball:** Predict a pitcher's next pitch based on count, runners on base, and previous 2 pitch types.
* **Football:** Predict offensive play calls (Run vs. Pass) based on down, distance, and field position.

---

## 📌 Project Roadmap

This repository is structured into multiple levels of increasing model complexity:

- [x] **Level 1 (Current):** Basic 1st-Order Markov Chain (remembers your immediate last move).


---

## ✨ Features

* **Instant Keyboard Shortcuts:** Press `1` (Rock), `2` (Paper), or `3` (Scissors) for high-speed play.
* **Real-time AI Model Training:** The Flask backend updates transition weights after every round.
* **Live Telemetry Feedback:** Track user score, AI win rate, predicted user move vs actual user move.
* **Clean Monospace GUI:** Modern, high-contrast UI designed for clarity and fast feedback.

---

## 📁 Repository Structure

```text
RPSMODEL/
└── levelone/
    ├── app.py              # Python Flask backend & 
    └── templates/
        └── index.html      # Monospace web interface + JS event listeners
