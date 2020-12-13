import pytest
import yaml
from pythoncode.calculator import Calculator

data = yaml.safe_load(open('./data.yml'))
calc = Calculator()


@pytest.fixture(scope="class")
def up_and_down():
    print("开始计算")
    yield
    print("结束计算")


@pytest.fixture(params=data['add']['data'], ids=data['add']['ids'])
def add_data(request):
    return request.param


@pytest.fixture(params=data['sub']['data'], ids=data['sub']['ids'])
def sub_data(request):
    return request.param


@pytest.fixture(params=data['mul']['data'], ids=data['mul']['ids'])
def mul_data(request):
    return request.param


@pytest.fixture(params=data['div']['data'], ids=data['div']['ids'])
def div_data(request):
    return request.param


@pytest.fixture()
def result_assert():
    def _result_assert(fuc: str, assert_data: list):
        a, b, expect = assert_data

        if fuc == 'add':
            return calc.add(a, b) == expect

        if fuc == 'sub':
            return calc.sub(a, b) == expect

        if fuc == 'mul':
            return calc.mul(a, b) == expect

        if fuc == 'div':
            return calc.div(a, b) == expect

    return _result_assert
