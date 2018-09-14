from weather import Weather
clima = Weather()
cidade = clima.lookup_by_location('edmonton')
condicao = cidade.condition()
temperatura = int(condicao.temp())
if temperatura < 32: print ('Congelando...')