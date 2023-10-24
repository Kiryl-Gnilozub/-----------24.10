import unittest
from unittest.mock import Mock

class CalculationEngine:
    def __init__(self, db_gate, db_connection):
        self.db_gate = db_gate
        self.db_connection = db_connection

    def calc(self, value):
        return self.db_gate.calculate(value)

    def process(self, data):
        return self.db_gate.process_data(data)

class CalculationEngineTest(unittest.TestCase):

    def test_calc(self):
        db_gate = Mock()
        db_connection = Mock()

        calculation_engine = CalculationEngine(db_gate, db_connection)


        db_gate.calculate.return_value = 42 
        db_connection.connect.return_value = True  


        result = calculation_engine.calc(10)


        self.assertEqual(result, 42)

    def test_process(self):
        db_gate = Mock()
        db_connection = Mock()

        calculation_engine = CalculationEngine(db_gate, db_connection)

        db_gate.process_data.return_value = True  
        db_connection.connect.return_value = True 

        result = calculation_engine.process("data")

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()