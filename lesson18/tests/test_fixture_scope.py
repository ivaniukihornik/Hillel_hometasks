import pytest


class TestFixtureScope1:

    @pytest.mark.smoke
    def test_1(self):
        print('C1_T1')

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_2(self):
        print('C1_T2')


class TestFixtureScope2:

    @pytest.mark.regression
    def test_1(self):
        print('C2_T1')

    def test_2(self):
        print('C2_T2')
