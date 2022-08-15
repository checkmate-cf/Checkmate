# Software Requirements

## Vision

What is the vision of this product?
To use python to build a chess game which will allow the user to play chess against someone. It would also allow the user to play against the computer via AI.

What pain point does this project solve?
User can pass time, cure boredom by playing the chess game, and level up your chess skills without needing a partner.

Why should we care about your product?
A free and accessible way to play chess on your computer, and it's fun. Plus you will get to see how talented our group is. You will want to hire the people who made the product.

## Scope of Project

### In

- Play chess against a person

- Play chess against AI

### Out

- Not a mobile app

- Can't play against another player online

### MVP

- CLI interface
  - Letters represent different pieces
  - [] is white, () is black, eg;[K]=a white king
  - "X" represents an empty space

- Ask if user wants to play against computer or AI

### Stretch

- Timer

- Multiple difficulties of AI

- User interface beyond the CLI
  - Allow user to choose color of chess pieces

- Save the game to come back to it

## Functional Requirements

- Refer to MVP: Allow user to play chess against human or AI

### Dataflow

- User starts the program

- User is welcomed to the game and prompted if the user wants to play against a human or AI

- Players take turns making moves, provding their moves making keyboard commands, eg: B2 B3

- Game continues, checkmate or stalemate occurs

- Upon completion user is prompted if they want to play again

## Non-Functional Requirements

### Tesability

- Provide automated tests using pytest that tests things such as:
  - Valid moves, eg: knight can only move in an L
  - Killing pieces
  - Check is correctly identified
  - Checkmate is correctly identified

### Usability

- Base usability:
  - CLI command and display or base functionality

- Stretch usability:
  - Interface with ability for drag and drop pieces
  - Uses mouse to control the game
  - user can choose color they want to be, eg: red or blue
  