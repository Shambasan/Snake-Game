# Snake-Game
snake game building with Animation ,coordinates , Inheritance & List slicing

Snake game using the Turtle graphics library.The game is set within a 600x600-pixel screen with a black background and titled "My Snake Game." 
It utilizes the Snake, Food, and Scoreboard classes to manage the snake's behavior, food generation, and game scoring, respectively. 
Keyboard controls are set up to respond to arrow keys for snake movement.
The game operates within a loop, continually updating the screen, moving the snake, and checking for collisions. 
Collisions with food result in score increments and snake lengthening, while collisions with screen borders lead to game-over conditions. 
Tail collisions are detected by iterating through snake segments, excluding the head. The game loop runs until the 'game_is_on' variable becomes False, and the screen exits upon user interaction. 
The code incorporates comments for clarity, offering alternative approaches for collision detection. Further enhancements, 
such as code organization and additional features, can be considered for future improvements.
