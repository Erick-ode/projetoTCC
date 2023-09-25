import unittest
from backend.src.main.models.questionnaire_processor import QuestionnaireProcessor
from backend.src.main.utils.settings import ANTECEDENTS_DATA


class TestQuestionnaireProcessor(unittest.TestCase):
    def setUp(self) -> None:
        self.response = {
            "attributes": {
                "time": [
                    {
                        "question_id": 0,
                        "field_name": "",
                        "answer": "6"
                    }
                ],
                "cost": [
                    {
                        "question_id": 0,
                        "field_name": "",
                        "answer": "Sênior:3;Pleno:5;Junior:8"
                    }
                ],
                "responsible": [
                    {
                        "question_id": 0,
                        "field_name": "",
                        "answer": "5"
                    },
                    {
                        "question_id": 1,
                        "field_name": "",
                        "answer": "sim"
                    }
                ],
                "explanation": [
                    {
                        "question_id": 0,
                        "field_name": "",
                        "answer": "ferramenta automatizada"
                    },
                    {
                        "question_id": 1,
                        "field_name": "",
                        "answer": "13"
                    }
                ]
            }
        }
        self.processor = QuestionnaireProcessor(self.response)

    def test_process_time(self):
        self.processor.process_time()

        self.assertEqual(self.processor.input_values['time'], 8.0)

    def test_process_cost(self):
        self.processor.process_cost()

        self.assertEqual(self.processor.input_values['cost'], 40.0)

    def test_process_responsible(self):
        self.processor.process_responsible()

        self.assertEqual(self.processor.input_values['responsible'], 4.5)

    def test_process_explanation(self):
        self.processor.process_explanation()

        self.assertEqual(self.processor.input_values['explanation'], 10.75)
