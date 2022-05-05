from typing import Union

import requests
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question
from .serialiazers import QuestionSerializer


def get_questions(questions_num: int) -> list:
    r = requests.get(f"https://jservice.io/api/random?count={questions_num}")
    return r.json()


def is_question_in_db(question_id: int) -> bool:
    """Checks if questions has already been written to DB"""
    return Question.objects.filter(question_id=question_id).exists()


def transform_into_list_of_questions(questions_data: list) -> list:
    """Transforms data from request.data into list of dicts with questions"""
    questions_to_check = []
    for idx, chunk in enumerate(questions_data):
        questions_to_check.append({})
        question_id = chunk.get("id")
        question = chunk.get("question")
        answer = chunk.get("answer")
        question_created = chunk.get("created_at")
        questions_to_check[idx]["question_id"] = question_id
        questions_to_check[idx]["question"] = question
        questions_to_check[idx]["answer"] = answer
        questions_to_check[idx]["question_created"] = question_created
    return questions_to_check


def serialize(
    questions_to_serializer: list, record_to_return: Union[dict, list]
) -> Response:
    serializer = QuestionSerializer(data=questions_to_serializer, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(record_to_return, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def questions(request):
    last_record = Question.objects.last()
    record_to_return = model_to_dict(last_record) if last_record else []
    questions_num = request.data.get("questions_num")
    questions_data = get_questions(questions_num)
    questions_to_check = transform_into_list_of_questions(questions_data)
    questions_to_serializer = []
    for question in questions_to_check:
        if is_question_in_db(question["question_id"]):
            questions_data_new = get_questions(1)
            question_to_check_new = transform_into_list_of_questions(questions_data_new)
            questions_to_check.extend(question_to_check_new)
        else:
            questions_to_serializer.append(question)
    return serialize(questions_to_serializer, record_to_return)
