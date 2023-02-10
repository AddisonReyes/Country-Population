import charts as ch
import csv

#Extraccion de la data del csv
def extraction_data(path):
	with open(path) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		header = next(reader)
		countries = []
		data = []

		for line in reader:
			data.append(dict(zip(header, line)))

		return(data)



def run():
	datos = extraction_data('./data.csv')
	selected_country = {}

	country = input('\nEscribe el nombre de un pais para extraer su informacion.\n\n\tPais: ')

	#Busqueda del pais
	for data in datos:
		if data['Country/Territory'].lower() == country.lower():
			selected_country = data

	if selected_country == {}:
		return print("\nError: Pais no encontrado...")

	#Busqueda de datos del pais
	years = []
	population = []

	print("\nLos datos del pais seleccionado son:")
	for datos in selected_country:
		print(f"\t{datos}: {selected_country[datos]}")

		try:
			int(datos[0:2])

			years.append(int(selected_country[datos]))
			population.append(datos[0:4])
		except:
			pass

	#Graficos
	ch.generate_bar_chart(population, years)
	ch.generate_pie_chart(population, years)
	

if __name__ == '__main__':
	run()