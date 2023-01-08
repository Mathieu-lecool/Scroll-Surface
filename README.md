# Scroll-Surface
A script to scroll a Pygame surface.
This script creates scrollable surfaces in your Pygame projects. The principle is the same as ScrollViews with the Kivy module.

# How to use
You must create a variable and assign the value "Scroll()" and insert the surface to be replaced.
```
scrollbar = Scroll(pygame.display.set_mode((200, 200))
```

To change the height of the scrollable surface, you need to change the height with **.height()**
```
scrollbar.height = 300
```

To get the scrollable surface, you must use ".get_screen()"
```
screen = scrollbar.get_screen()
```

# Exemple
```
import pygame

# import Scroll()


scrollbar = Scroll(pygame.display.set_mode((200, 200)))
scrollbar.height = 300

screen = scrollbar.get_screen()

while True:
    screen.fill((0,255,0))

    for i in range(30): pygame.draw.rect(screen, (0,0,255), pygame.Rect(0, i*10, 200, 5))

    scrollbar.update()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEWHEEL:
            scrollbar.mousewheel(event)
```
