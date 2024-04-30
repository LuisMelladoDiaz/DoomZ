# Doom Zombies
<img src="https://github.com/LuisMelladoDiaz/DoomZ/blob/main/images/DoomZ.jpg" alt="Conceptual art" width="400">

# Project State

## Game Engine

### v0_27_04_2024
The game engine was developed following the [tutorial](https://www.youtube.com/watch?v=huMO4VQEwPc&t=1s) create by 3DSage, plaese suscribe to his [channel](https://www.youtube.com/@3DSage) and have a look at the original work.

3DSage developed this engine in C so it was my work to port it to python. I do not know C so the port was developed by understanding and translating the ideas and following my intuition. That means that even though I tried to refactor and optimize the code for python there is still room for improvement. If you find any mistakes or you think the code can be rewritten to run more efficiently, do not doubt in contacting me or sending a pull request if you feel like it.

This is how the game engine looks at the moment:   

     
<img src="https://github.com/LuisMelladoDiaz/DoomZ/blob/main/images/GameEngine_v0.png" alt="Conceptual art" width="400">


### Map editor v0_01_05_24
The map editor was inspired by 3DSage [work](https://www.youtube.com/watch?v=fRu8kjXvkdY). This time I did not port his code to python, I took the idea and coded it completely on my own. At this point in time the map editor has a lot of limitations and it is intendended to be expanded with more functionalities. However, with this version is enough to start building some simple maps to test the game engine.     

![Map editor showcase](https://github.com/LuisMelladoDiaz/DoomZ/assets/93400291/4c1825eb-b67e-41c2-8924-82ebe2209af5)     

To build a map in the editor:
1) Go to the folder map and run mapEditor.py.
2) A grid like GUI will show up. Notice a sidebar with options. The only working feature right now is "Wall color".
3) Start drawing dots in the grid by clicking. Every two dots form a Wall of color "Wall color".
4) Draw as many walls as you want. Finally click on the first dot you drew to close the Sector.
5) Draw as many sectors as you desire.
6) Hit save. Exit map folder and run main.




