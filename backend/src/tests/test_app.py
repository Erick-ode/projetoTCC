from backend.src.main.app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_root_source(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_tecnic(self):
        response = self.app.get('/retornar_tecnica')
        self.assertEqual(response.status_code, 200)

    def test_post_answers(self):
        json_data = {
            "time": 12.795258311882149,
            "cost": 175.8650745039662,
            "responsible": 14.92867659725409,
            "explanation": 47.456611622484715,
            "reliability": 126.49172709989107,
            "patronization": 1.446144933550861,
            "productivity": 66.4520288668543
        }

        response = self.app.post('/processar_respostas', json=json_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
