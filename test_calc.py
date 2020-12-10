import pytest
import allure
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @allure.feature("Calculator Add Feature Testcase")
    @pytest.mark.parametrize("a,b,expect", [
        (0, 0, 0), (0, 1, 1), (3, 5, 8), (-1, -2, -3), (3.52, 7.6, 11.12), (100, 300, 400)
    ], ids=["zero", "zero+int", "int", "minus", "float", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @allure.feature("Calculator Sub Feature Testcase")
    @pytest.mark.parametrize("a,b,expect", [
        (0, 0, 0), (0, 1, -1), (5, 3, 2), (3, 5, -2), (-1, 2, -3), (3, -1, 4), (-1, -2, 1), (7.6, 3.52, 4.08),
        (3000, 1000, 2000)
    ], ids=["zero", "zero-positive", "positive", "negative", "negative-positive", "float", "positive-negative",
            "negative-negative", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @allure.feature("Calculator Mul Feature Testcase")
    @pytest.mark.parametrize("a,b,expect", [
        (0, 0, 0), (0, 1, 0), (0, -1, 0), (3, 5, 15), (-1, 2, -2), (-1, -2, 2), (7.6, 3.52, 26.752), (100, 300, 30000)
    ], ids=["zero", "zero*int", "zero*negative", "positive*positive", "negative*positive", "float", "negative*negative",
            "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @allure.feature("Calculator Div Feature Testcase")
    @pytest.mark.parametrize("a,b,expect", [
        (0, 0, "Error"), (0, 1, 0), (1, 1, 1), (7, 2, 3.5), (-4, 2, -2), (4, -2, -2), (-4, -2, 2), (40000, 200, 200)
    ], ids=["zero", "zero/int", "self/self", "float", "negative/positive", "positive/negative", "negative/negative",
            "bigint"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)
