import pytest
import allure


@allure.title("计算器冒烟测试")
@allure.feature("Calculator Function")
@pytest.mark.usefixtures("up_and_down")
class CalcCases:

    @allure.story("Add Feature Testcase")
    @allure.title("加")
    @allure.severity("critical")
    @pytest.mark.run(order=1)
    @pytest.mark.add
    def calc_add(self, result_assert, add_data):
        assert result_assert("add", add_data)

    @allure.story("Sub Feature Testcase")
    @allure.severity("blocker")
    @allure.title("减")
    @pytest.mark.run(order=2)
    @pytest.mark.sub
    def calc_sub(self, result_assert, sub_data):
        assert result_assert("sub", sub_data)

    @allure.story("Mul Feature Testcase")
    @allure.title("乘")
    @allure.severity("normal")
    @pytest.mark.run(order=3)
    @pytest.mark.mul
    def calc_mul(self, result_assert, mul_data):
        assert result_assert("mul", mul_data)

    @allure.story("Div Feature Testcase")
    @allure.title("除")
    @allure.severity("normal")
    @pytest.mark.run(order=4)
    @pytest.mark.div
    def calc_div(self, result_assert, div_data):
        assert result_assert("div", div_data)