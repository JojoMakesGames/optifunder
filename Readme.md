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

I only have tests for the functional part of the exersize and kept it pretty light. There should be testing around main, but I wanted to keep this to around a couple hours like y'all said.

