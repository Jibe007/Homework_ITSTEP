import json
from product import Product

product1 = Product("Laptop", "1000.0 GEL", 10)
product2 = Product("Smartphone", "700.0 GEL", 25)
product3 = Product("Headphones", "150.0 GEL", 50)

products = [product1, product2, product3]

with open("products.json", "w") as file:
    json.dump([product.to_dict() for product in products], file, indent=4)

with open("products.json", "r") as file:
    product_data = json.load(file)

deserialized_products = [Product.from_dict(item) for item in product_data]

for product in deserialized_products:
    print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

#-------------Davaleba 2--------------


with open('movies.json', 'r') as file:
    data = json.load(file)

updated_movies = []

for movie in data:
    if 'results' in movie:
        for movie_detail in movie['results']:
            release_year = int(movie_detail['release_date'][:4])
            genres = movie_detail['genres']

            if release_year > 2000 and 'Crime' in genres:
                genres = ['New_Crime' if genre == 'Crime' else genre for genre in genres]
            elif release_year < 2000 and 'Drama' in genres:
                genres = ['Old_Drama' if genre == 'Drama' else genre for genre in genres]
            elif release_year == 2000:
                genres.append('New_Century')

            movie_detail['genres'] = genres

            updated_movies.append(movie_detail)

with open('movies.json', 'w') as file:
    json.dump(data, file, indent=4)
