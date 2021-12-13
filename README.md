# StarWars blog database

**Important**: To do this activity you need to `fork` this repo into your **Github** account and then open the forked repo on Gitpod.

Inside he `src/models.py` file you will find a couple of classes describing an example database.

Here is a 4min video explaining what UML is: [https://www.youtube.com/watch?v=UI6lqHOVHic](https://www.youtube.com/watch?v=UI6lqHOVHic)

We are going to be creating the Entity Relationship Diagram for your StarWars Blog Database, a very similar diagram to this one:

![Starwars Diagram](https://github.com/breatheco-de/exercise-starwars-data-modeling/blob/master/assets/example.png?raw=true)
[Click to open diagram](https://app.quickdatabasediagrams.com/#/d/LxNXQZ)

> 🔥 You can use this FREE tool to practice your diagram for the first time: https://app.quickdatabasediagrams.com/#/d/

## 💻 Installation

1. Get inside the environment `$ pipenv shell`

2. Install all dependencies `$ pipenv install`

3. Generate de diagram as many times as you need `$ python src/models.py`

4. Open the file `diagram.png` to check out your UML diagram!


## 📝Instructions

Your Job is to update the `src/models.py` file with the code needed to replicate the Starwars data model.

The project is using the SQLAlchemy Python library to generate the database.

- Your project must have a table `User` that will represent your blog users.
- Your blog users will be able to login and save their favorite planets and characters.
- The database should store the user favorites.
- The database should store characters and planets.
- What other tables do you think a blog like this might have?
- What properties should go inside the user? or inside the Character or Favorite table?
- What are the relationships between those tables?
- Please add at least 4 models with all of its properties.
- Generate the diagram.png file at the end by running `$ python3 models.py` on the console.


