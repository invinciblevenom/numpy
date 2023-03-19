# Made a dataset of 10 countries with there GDP. Printed the name of country with highest per capita gdp and lowest per
# capita gdp. Also found the mean, standard deviation and sum of per capita gdp of all countries. 


import numpy as np
countries = np.array(['China', 'India', 'Pakistan', 'Sri Lanka', 'Nepal', 'Bhutan', 'Bangladesh', 'USA',
                      'UK', 'Russia'])
gdp_per_capita = np.array([225.25, 629.71, 350.74, 195.38, 99.29, 45.12, 38.75, 459.53, 550.98, 614.48])
max_gdp_per_capita = gdp_per_capita.argmax()
country_with_max_gdp_per_capita = countries[max_gdp_per_capita]
print("Country with max gdp per capita is", country_with_max_gdp_per_capita)

min_gdp_per_capita = gdp_per_capita.argmin()
country_with_min_gdp_per_capita = countries[min_gdp_per_capita]
print("Country with min gdp per capita is", country_with_min_gdp_per_capita)

for country in countries:
    print('ecaluating country {}'.format(country))

for i in range(len(countries)):
    country = countries[i]
    country_gdp_per_capita = gdp_per_capita[i]
print('country {} per capita gdp is {}'.format(country, country_gdp_per_capita))

print(gdp_per_capita.max())
print(gdp_per_capita.min())
print(gdp_per_capita.mean())
print(gdp_per_capita.std())
print(gdp_per_capita.sum())
