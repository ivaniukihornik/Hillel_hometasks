# 5 тестів, знаходяться в класі. Тести можуть бути пусті (pass).
# На кожному тесті мітка (mark) 'from_class'. Перед тестами та після них має відпрацювати фікстура,
# яка виведе повідомлення про початок тестів, та про їх завершення. Має бути одне повідомлення про початок,
# та одне повідомлення про завершення тестів.
from pytest import mark


class TestsClass:
    @mark.from_class
    def test_1_part_1(self):
        pass

    @mark.from_class
    def test_2_part_1(self):
        pass

    @mark.from_class
    def test_3_part_1(self):
        pass

    @mark.from_class
    def test_4_part_1(self):
        pass

    @mark.from_class
    def test_5(self):
        pass
