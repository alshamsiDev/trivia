import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}@{}/{}".format('postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.new_question = {
                'question': 'What is your best moment in 2020',
                'answer': 'Get a job',
                'difficulty': 5,
                'category': 3,
            }
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    def test_i_can_see_all_question(self):
        res = self.client().get('/questions?page=2')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))

    def test_throw_error_if_page_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Resource not found')

    def test_i_can_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_throw_error_if_user_delete_not_exist_question(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def test_i_can_create_a_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)
        self.assertTrue(data['created'])

    def test_throw_error_if_new_question_did_not_proceed(self):
        res = self.client().post('/questions', json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_i_can_search_for_a_word_and_see_all_questions_that_matches_the_search(self):
        res = self.client().post('/search', json={'searchTerm': 'author'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_throw_error_search_for_a_word_and_see_all_questions_that_does_not_matches_the_search(self):
        res = self.client().post('/search', json={'searchTerm': 'Say my name'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_i_can_filter_question_based_on_category(self):
        res = self.client().get('/categories/2/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_i_cannot_filter_question_based_on_unlisted_category(self):
        res = self.client().get('/categories/40/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)

    def test_i_can_play_quiz_and_see_my_result_at_the_end(self):
        res = self.client().post('/quizzes',
                                 json={'previous_questions': [], 'quiz_category': {'id': '3'}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_throw_error_play_quiz_with_unlisted_category(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'id': '9'}})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
