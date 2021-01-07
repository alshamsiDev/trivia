import os
from flask import Flask, request, abort, jsonify, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE_PER_SHELF = 10


def paginate_questions(req, selection):
    page = req.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE_PER_SHELF
    end = start + QUESTIONS_PER_PAGE_PER_SHELF
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def homepage():
        return redirect(url_for('index_questions'))

    @app.route('/categories')
    def index_categories():
        categories = Category.query.all()
        return jsonify({
            'success': True,
            'categories': {category.id: category.type for category in categories},
        })

    @app.route('/questions')
    def index_questions():
        questions = Question.query.all()
        current_questions = paginate_questions(request, questions)
        if len(current_questions) == 0:
            abort(404)

        categories = Category.query.all()
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(questions),
            'categories': {category.id: category.type for category in categories},
        })

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.get(id)
            if question is None:
                abort(404)
            question.delete()
            return jsonify({
                'success': True,
                'deleted': question.id,
            })

        except:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def post_question():
        body = request.json
        if body == {}:
            abort(422)
        question = body.get('question', None),
        answer = body.get('answer', None),
        category = body.get('category', None),
        difficulty = body.get('difficulty', None)
        try:
            question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
            question.insert()
            return jsonify({
                'success': True,
                'created': question.id,
            })
        except:
            abort(422)

    @app.route('/search', methods=['POST'])
    def search():
        search = request.get_json().get('searchTerm', None)
        try:
            search_results = Question.query.filter(Question.question.ilike(f'%{search}%')).all()
            print(search_results)
            if not search_results:
                abort(404)
            return jsonify({
                'success': True,
                'questions': [question.format() for question in search_results],
                'total_questions': len(search_results),
                'current_category': None
            })
        except:
            abort(422)

    @app.route('/categories/<int:id>/questions')
    def questionsByCategories(id):
        category = Category.query.get(id)
        if category is None:
            abort(400)
        question_category = Question.query.filter(Question.category == category.id).all()
        current_questions = paginate_questions(request, question_category)
        print(len(current_questions))
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(current_questions),
            'current_category': category.id
        })

    @app.route('/quizzes', methods=['POST'])
    def play():
        try:
            category = request.get_json().get('quiz_category', None)
            prev_questions = request.get_json().get('previous_questions', None)
            questionQuery = ''
            questions = []
            if category is None or prev_questions is None:
                abort(404)
            if category['id'] == 0:
                questionQuery = Question.query.all()
            elif Category.query.get(category['id']) is not None:
                questionQuery = Question.query.filter(Question.category == category['id']).all()
            else:
                abort(422)

            for question in questionQuery:
                if question.id not in prev_questions:
                    questions.append(question)

            if len(questions) == 0:
                new_question = None
            else:
                new_question = questions[random.randrange(0, len(questions))].format()
            print(new_question)
            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable '
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    return app
