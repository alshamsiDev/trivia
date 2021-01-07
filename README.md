# Trivia Project

## Simple CRUD project

Trivia is a fun project that shows you all questions, and you can test your knowledge by visit play tab to test answer
all questions.

## API Documentation

### Routes

#### GET ROUTES

1. `/questions` - GET OR `/questions?page="number"` - GET with pagination

Returns a list questions.

Sample of response

`{
"categories": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
},
"questions": [
{
"answer": "George Washington Carver",
"category": 4,
"difficulty": 2,
"id": 12,
"question": "Who invented Peanut Butter?"
}, {
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
}, {
"answer": "The Palace of Versailles",
"category": 3,
"difficulty": 3,
"id": 14,
"question": "In which royal palace would you find the Hall of Mirrors?"
}, {
"answer": "Agra",
"category": 3,
"difficulty": 2,
"id": 15,
"question": "The Taj Mahal is located in which Indian city?"
}, {
"answer": "Escher",
"category": 2,
"difficulty": 1,
"id": 16,
"question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
}, {
"answer": "Mona Lisa",
"category": 2,
"difficulty": 3,
"id": 17,
"question": "La Giaconda is better known as what?"
}, {
"answer": "One",
"category": 2,
"difficulty": 4,
"id": 18,
"question": "How many paintings did Van Gogh sell in his lifetime?"
}, {
"answer": "Jackson Pollock",
"category": 2,
"difficulty": 2,
"id": 19,
"question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
}, {
"answer": "The Liver",
"category": 1,
"difficulty": 4,
"id": 20,
"question": "What is the heaviest organ in the human body?"
}, {
"answer": "Alexander Fleming",
"category": 1,
"difficulty": 3,
"id": 21,
"question": "Who discovered penicillin?"
}
],
"success": true,
"total_questions": 14 }`

2. `/categories/` - GET

Returns a list categories.

Sample of response

`{
"categories": {
"1": "Science",
"2": "Art",
"3": "Geography",
"4": "History",
"5": "Entertainment",
"6": "Sports"
},
"success": true }`

3. `/categories/<id>/questions` - GET

Returns a list of Questions based on the given categories.

Sample of response

`{
"current_category": 1,
"questions": [
{
"answer": "The Liver",
"category": 1,
"difficulty": 4,
"id": 20,
"question": "What is the heaviest organ in the human body?"
}, {
"answer": "Alexander Fleming",
"category": 1,
"difficulty": 3,
"id": 21,
"question": "Who discovered penicillin?"
}, {
"answer": "Blood",
"category": 1,
"difficulty": 4,
"id": 22,
"question": "Hematology is a branch of medicine involving the study of what?"
}
],
"success": true,
"total_questions": 3 }`

### POST ROUTES

1. `/questions` - POST

Send a request to the server to create new question

Sample of response

`{
"created": 72,
"success": true }`

2. `/search` - POST

Send a request to the server to filter out question based on the term given in the body

sample of response

`{
"current_category": null,
"questions": [
{
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
}
],
"success": true,
"total_questions": 1 }`

3. `/quizzes` - POST

Allows users to test their knowledge by play a simple fun quiz game.

Returns new question every time and save the old ones in the previous questions.

`{
"question": {
"answer": "Lake Victoria",
"category": 3,
"difficulty": 2,
"id": 13,
"question": "What is the largest lake in Africa?"
},
"success": true }`

### DELETE ROUTES

3. `/questions/<id>/` - DELETE

Delete a specific questions based on the given id.

Sample of returned response

`{
"deleted": 17,
"success": true }`

## Project structure and how to install it

### structure

The project consist of two folders.

`Frontend` where it holds all the frontend stuff, and the code

`Backend` where it has the all the code for the backend

### Tools

- React.js
- Flask
- Postgresql

## how to install and use the project:

* Fork the project repository and Clone your forked repository to your machine.

* cd to frontend and open terminal, and paste `npm i && npm start`
* `cd ..` to go back to the root
* cd to backend and open terminal, and paste `pip3 install -r requirements.txt && FLASK_APP=flaskr FLASK_DEBUG=true flask run `

Now your frontend and backend should be working as expected.

## Future improvements
- Support Arabic language
- Deploy it on the heroku 