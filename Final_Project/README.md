This is my final project for CS50 Python course. It's gonna be a UI character creator.

I will be using Panda3D for 3D and PyQT6 for UI stuff.

The plan is to let user create not only the base character look, but also give him name, story, stats etc. and then let him export it so it would be actually usable in my future game.

The biggest challenge for now (I think) is 3D character modification via code. I never done that before, but it interest me very much.

I will be using synty's assets, because I like them and there are lots of them in the same style.

Another task is to somehow get separated clothes from assets, for now from what I see in packs like military there are only full outfits, so I will need to make a program to cut them for parts so I could let user choose from these parts and join them again.

The base wokrflow for code character creation is to just prepare all the parts with valids origin points and then also have a manequin with x,y,z positions where specific parts of outfit (their origin points) should be.

My inspiration for creator is Project Zomboid's creator where you have to balance between positive and negative traits to create interesting characters with story. 

If I will not be able to create UI part and 3D part at once, then I will just add 3D later as V2 of the app.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Soooo, how to design that v1 part? What do I need? 
Well, I will need pictures of clothes so player can choose from them, but how do I do that? do I want them to be in t-pose? or maybe scrap pictures and just make a list? naah
Welp, I will definitely at some point need clothes in t-pose, but I need to think of a mass solution...

Okay so something like: get character to blender -> somehow get them in t-pose -> somehow cut it for parts -> somehow add origin points (or it may be auto) -> somehow focus on every part step by and then take a pic of it -> save pics, parts, etc


Also, do i somehow fake preview with 2D look or go with 3D render at start?? Maybe do something like in Tarkov, that UI with human drawing in the back and empty boxes on parts of the body where you put clothes?? and then button for render? and then play basic idle animation? 