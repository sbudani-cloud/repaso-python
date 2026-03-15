from city_functions import city_country

def test_city_country():
    resultado = city_country('santiago', 'chile')
    assert resultado == 'Santiago, Chile'


def test_city_country_population():
    resultado = city_country('santiago', 'chile', population=5000000)
    assert resultado == 'Santiago, Chile – población 5000000'