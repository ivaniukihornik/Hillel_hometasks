# Тести потрібно запускати через клас, інакше порушиться логіка і вони будуть валитись
class TestIphone:
    # Перевіряю, чи правильно додається айфон
    def test_item_creation(self, iphone):
        print('\nModel: {}'
              '\nPrice: {}'
              '\nUnits sold: {}'
              '\nTotal units sold: {}'.format(iphone.model, iphone.price, iphone.units_sold,
                                              iphone.total_units_sold[iphone.model]))
        assert all([iphone.model == 'Iphone 14 Pro Max', iphone.price == 899, iphone.units_sold == 15000])

    # Чи правильно оновлюється показник проданих товарів
    def test_units_updating(self, iphone):
        iphone.update_units_sold(3500)
        print(f'\nUnits sold (після оновлення): {iphone.units_sold}')
        assert all([iphone.units_sold == 18500, iphone.total_units_sold[iphone.model] == 18500])

    # Чи правильно вираховується показник прибутку компанії Apple після продажу айфонів
    def test_income_obtaining(self, company, iphone):
        company.update_revenue(iphone.get_income())
        print(f'\n{company}')  # Можна вивести стан об'єкту Apple, щоб подивитися прибуток компанії
        # після продажу айфонів
        assert company.revenue == 16_631_500

    # Чи обнуляється показник проданих одиниць товару після перерахунку прибутку компанії та чи не змінюється лічильник
    # загальної кількості проданих одиниць
    def test_units_updating_after_revenue_updating(self, iphone):
        print(f'\nUnits sold (після підрахунку прибутку): {iphone.units_sold}'
              f'\nTotal units sold (після підрахунку прибутку): {iphone.total_units_sold[iphone.model]}')
        assert all([iphone.units_sold == 0, iphone.total_units_sold[iphone.model] == 18500])
