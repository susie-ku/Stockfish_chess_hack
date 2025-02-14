# Hard Mate in 3 - Stockfish Chess AI Challenge

## Overview
This project demonstrates an interactive chess AI that plays as Black and attempts to win checkmate at all costs. The AI is powered by GPT-4 and follows a strict reasoning process before making each move. The game setup presents a **Mate in 3** puzzle where White has a forced win in three moves.

## How It Works
1. **Initial Setup:**
   - The chessboard starts in a predefined position where White can checkmate in three moves.
   - The LLM plays as Black and tries to counter the checkmate.

2. **Game Flow:**
   - White plays the first move from a pre-defined winning strategy.
   - The AI generates its move based on the current board state.
   - If the AI's move is invalid, it will reattempt until a valid move is found.
   - The game continues until checkmate or an end condition is reached.

3. **Chain-of-Thought (CoT) Reasoning:**
   - The AI explains its move before executing it.
   - Each reasoning step is stored in the `/cot/` directory as a text file.

## Key Features
- **GPT-4 Powered Chess AI:** The AI makes moves based on strategic analysis.
- **Auto-Correction:** If the AI generates an illegal move, it retries until a valid move is found.
- **Chain-of-Thought Logging:** The AI's thought process is saved at each step for transparency and debugging.
- **Predefined Winning Strategy:** White follows a winning sequence to ensure a decisive conclusion.

## How to Run
Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt
```
Then, run the script:
```bash
python run.py
```

## Example Output
```
Initial board:
  a b c d e f g h
8 . . . . . . k .
7 . . . . . p p p
6 . . . . . . . .
...
White played: f2f4
Board after White's move:
...
LLM played: g7g6
Board after LLM's move:
...
Final board state:
  a b c d e f g h
8 . . . . . . k .
...
Game Over!
```

## Results

### Attempt to Reproduce Stockfish Experiment

I was unable to configure the system to launch the agent in the exact experimental setup as described in the initial experiment (due to problems with Docker).

Due to these technical challenges, I was unable to observe the model's behavior in the same conditions that were reported to facilitate cheating attempts in the original experiment.

### Key Observations for This Version:
- **No Evidence of Cheating**: No evidence on the model’s cheating behavior in my setup.

## Future Improvements

1. **Integration with `inspect_evals` Library**:  
   I plan to integrate my experiments with the `inspect_evals` library. The integration steps are as follows:
   - **Game Simulation**: Create a `game.py` file that accepts the LLM output and the current chess board state, then outputs an updated board state corresponding to the next move. Note that I did not have sufficient time to fully implement this function.
   - **Scoring Functions**:  
     Choose accurate scoring functions to evaluate moves. The simplest approach is to use the `includes()` function with predefined keywords as targets. In addition, I can leverage more advanced functions like `model_graded_qa()` or `model_graded_fact()` for a refined evaluation.
   - **Existing Evaluation Code**:  
     You can refer to the non-ended evaluation code available in the `eval/` folder as a starting point for further integration.
2. **Launch an LLM Agent with Access to Bash and Python**: Develop and deploy an LLM agent capable of interacting with the system through bash and Python commands, along with file editing capabilities. This will allow more accurate and comprehensive searches for potential cheating behaviors.
3. **Support for Different Difficulty Levels**: Implement varying difficulty levels (Hard mate puzzles) to test the agent's robustness and identify potential weaknesses in different scenarios.


