# Using this project
Run these commands
* poetry install
* tests: poetry run pytest project/test.py
* code: poetry run python project


# Choices
I chose a bit more of a functional approach here. Since it's not really something getting passed around and just
an object modifier, it felt like it was best to distinctly define the functions and have them do exactly
as they say.

However, I did lay out what the classes could look like if that was the route that we needed to go. I've found
that namedTuples often are good for one off bits like this, however the fact that the definitions all need to be the exact
same for this definition makes classes maybe more appealing. 

I only have tests for the functional part of the exercise and kept it pretty light. There should be testing around main, but I wanted to keep this to around a couple hours like y'all said.

The dictionary format that I'm using should allow any developers to easily add more functionality. And then checking the input to see if it's valid before really separates the concern/error handling with the main function that is called. There's an exception catcher just in case something happens, that way the app doesn't crash.

Obvious improvements are persisting the data or allowing an object to be passed in to start. But it didn't seem like that was the scope of the project.

