# 3 (або більше) тести, організовані довільно (в класі чи поза ним). На кожному тесті 2 мітки: одна спільна для усіх
# тестів в цьому пакунку, наприклад 'pack', друга -- спільна для частини тестів, наприклад для двох;
# остання 'rest' -- для тих тестів що залишились.
from pytest import mark


@mark.main
@mark.pack
def test_1_part_3():
    pass


@mark.main
@mark.pack
def test_2_part_3():
    pass


@mark.rest
@mark.pack
def test_3_part_3():
    pass


@mark.rest
@mark.pack
def test_4_part_3():
    pass
