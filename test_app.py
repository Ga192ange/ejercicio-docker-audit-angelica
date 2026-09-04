import unittest

from app import app


class TestHealthCheck(unittest.TestCase):

    def test_health_check(self):
        cliente = app.test_client()

        for _ in range(5):
            respuesta = cliente.get("/health")
            self.assertEqual(
                respuesta.status_code,
                200,
                "El servicio de salud es inestable"
            )


if __name__ == "__main__":
    unittest.main()