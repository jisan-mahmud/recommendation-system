import csv
import ast
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recommendation.settings')
django.setup()
from products.models import Product

with open('flipkart_com-ecommerce_sample.csv', mode='r', encoding="utf-8") as file:
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    for row in reader:
        try:
            name = row[3]                      # product name
            category = row[4].strip()         # category
            price = row[7]                    # discounted price
            description = row[10]             # description
            
            # Extract first image URL
            image_list = ast.literal_eval(row[8])
            image_url = image_list[0] if image_list else None

            product = {
                "name": name,
                "image": image_url,
                "description": description,
                "category": category,
                "price": price,
            }
            
            Product.objects.get_or_create(**product)
            print('complete!')
        except Exception as e:
            print("Error parsing row:", e)
