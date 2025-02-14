#!/usr/bin/env python3

import openai
import chess
import chess.svg
import sys

def get_legal_moves(board: chess.Board):
    return [move.uci() for move in board.legal_moves]

def query_llm(board: chess.Board, api_key: str, model="gpt-4"):
    legal_moves = get_legal_moves(board)
    board_fen = board.fen()
    
    prompt = f"""
    Given the following chess position in FEN notation:
    {board_fen}
    
    And the list of legal moves:
    {', '.join(legal_moves)}
    
    Suggest the best move and explain why.
    """
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a chess expert."},
                  {"role": "user", "content": prompt}],
        api_key=api_key
    )
    
    return response["choices"][0]["message"]["content"]

def main(api_key):
    board = chess.Board()
    return query_llm(board, api_key)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./llm_chess.py <API_KEY>")
        sys.exit(1)
    
    api_key = sys.argv[1]
    print(main(api_key))
