
# PyGame Setup

## Instructions

*In typical development environments, we'll want to install PyGame using what's called a package manager. In standard Python installations, you'll use a package manage called "pip". Luckily for us, Replit uses a package manager called poetry. Poetry will automatically download and install any dependencies (external libraries that we import into our code base is called a dependancy).*

1) Initialize Pygame

    In python we use the "import" statement to bring in modules or packages from external files or libraries into our script.

    We then initalize pygame by calling "pygame.init()":

    ```python
    import pygame
    pygame.init()
    ```

2) Create a game window

    We can create a Pygame window by calling "pygame.display.set_mode()" and passing the width and height as a tuple:

    ```python
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    ```

3) Start the main game loop

    Pygame typically runs within a main game loop. This loop keeps the game running handles all of the game events, such as user input, updating the game state and drawing graphics.

    ```python
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update Game State

        # Draw graphics

        pygame.display.update()
    
    pygame.quit()
    ```

4) Additional steps

    - We can even set the title of the Pygame window using "pygame.display.set_caption()"
    - 