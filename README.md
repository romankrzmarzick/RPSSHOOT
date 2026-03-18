# RPS SHOOT 🖖

RPS SHOOT is a highly modular, advanced terminal-based implementation of Rock-Paper-Scissors-Lizard-Spock, written entirely in Python. 

While it functions as a playable game, under the hood, it serves as an exploration of Object-Oriented Programming (OOP) architecture, structural design patterns, and statistical Artificial Intelligence.

## 🚀 Features

- **Dynamic Game Engine:** Play classic Rock-Paper-Scissors or the expanded 5-move "Lizard Spock" variation.
- **Advanced AI Opponents:** Battle against 4 different AI algorithms, ranging from purely random to a predictive, 2nd-order statistical Markov Chain.
- **Beautiful Terminal UI:** Built with the `rich` Python library for a styled, color-coded, and interactive command-line experience.
- **Robust Data Tracking:** The game tracks and calculates match history, win percentages, and your most/least successful moves.
- **Tiebreaker Logic:** Matches are played as a "Best-of" series. If a match ends in a tie, a "Win-by-Two" sudden-death tiebreaker automatically initiates.

## 🧠 The AI Opponents

The computer opponent is built using the **Strategy Pattern**, allowing it to swap "brains" based on user selection dynamically:

1. **Random AI:** The baseline bot. It picks a completely random valid move every turn.
2. **Common AI:** A basic analytical bot that finds the player's most frequently used move overall and plays its exact counter.
3. **Counter AI:** A reactive bot that simply looks at the player's *last* move and assumes they will play it again, playing the counter.
4. **Markov AI:** The "Boss" bot. It utilizes a 2nd-Order Markov Chain to build a statistical model of the player's habits. It looks at the player's last two moves, calculates the probability of their third move based on historical data, and throws the exact counter.

## 🏗️ Architecture & Code Quality

This project was built with a focus on clean, scalable software engineering principles:
- **Separation of Concerns:** The codebase is strictly divided into `main.py` (orchestration), `ui.py` (presentation), `data.py` (state management), and `game_rules.py` (logic).
- **The Factory Pattern:** AI models are instantiated dynamically via dictionary lookups rather than massive `if/else` blocks.
- **Automated Testing:** The logic is verified using a comprehensive `pytest` suite, including edge-case handling, integration tests, and user-input mocking via `@patch`.

## 🎮 How to Play

### Prerequisites
You will need Python 3 installed, along with the `rich` library for the terminal UI.

```bash
# Install the required UI library
pip install rich
