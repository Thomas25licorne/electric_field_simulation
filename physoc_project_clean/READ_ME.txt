Window: The interface of the pygame window
Screen: The gray area in the pygame window


-------------------------- FOR THE USER --------------------------

How does it work?

    - Run main.py

    - You will see the interface. On the right of the screen, click either the blue (point charge),
        the yellow (plane), the green (rod) or the orange (disk)

    - On the left side of the screen, set up its sign (red for positive or blue for negative)

    - Under the screen, set up its charge. If you want to go an exponent up, click the green button 
        on the right of the charger. Click the red button on its left to go an exponent down

    - If it's a point_charge:
        - Click the screen where you want the center of it to blue
    - If it's a plane:
        - Click the screen where you want one of the rectangle's corner to start. Click another in a different position. These two 
          coordinates will form the 2 opposite diagonal corners of the rectangle.
    - If it's a rod:
        - Similar to the plane, but it is a bit buggy. To make sure that you get what you want, start with the top left corner of the 
          rod (its width is fixed).
          If you want the rod to be horizontal, click the screen a second time more on the right than down
          If you want the rod to be vertical, click the screen a second time more down than on the right

    - If it's a disk:
        - Click a first time in the screen to mark the center of the disk. Click a second time to determine its radius

    - If ever you want to go back, click the red button on the top left of the window. (It may bug a little bit)

    - If you are satisfied with the screen, click the red button on the bottom right to send the values to matplotlib



----------------------------------------------------------------------------









