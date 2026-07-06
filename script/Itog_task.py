purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases:dict) -> float:
    sum = 0
    for i in purchases:
        if i.get("price", 0) == 0:
            print("Цена не указана")
        else:
            sum += i.get("price") * i.get("quantity")
    print(f"Общая выручка: {sum}")

def items_by_category(purchases:dict) -> dict:
    result = {}
    uniq_categories = {categ["category"] for categ in purchases if "category" in categ}
    for i in purchases:
        if i.get("category") in uniq_categories:
            result.setdefault(i.get("category"), []).append(i.get("item"))
    print(f"Товары по категориям: {result}")

def expensive_purchases(purchases:dict, min_price:float) -> list:
    result_list = []
    for i in purchases:
        if i.get("price") > min_price:
            result_list.append(i)
    print(f"Покупки дороже {min_price}: {result_list}")

def average_price_by_category(purchases:dict) -> dict:
    categ_with_price = {}
    result = {}
    uniq_categ = {categ["category"] for categ in purchases if "category" in categ}
    for i in purchases:
        if i.get("category") in uniq_categ:
            categ_with_price.setdefault(i.get("category"), []).append(i.get("price"))
    for i in categ_with_price:
        result[i] = sum(categ_with_price.get(i))/len(categ_with_price.get(i))
    print(f"Средняя цена по категориям: {result}")

def most_frequent_category(purchases:dict):
    categ_with_quantity = {}
    result = {}
    uniq_categ = {categ["category"] for categ in purchases if "category" in categ}
    for i in purchases:
        if i.get("category") in uniq_categ:
            categ_with_quantity.setdefault(i.get("category"), []).append(i.get("quantity"))
    for i in categ_with_quantity:
        result[i] = sum(categ_with_quantity.get(i))
    max = result.get(next(iter(result)))
    max_categ = next(iter(result))
    for i in result:
        if max < result.get(i):
            max_categ = i
    print(f"Категория с наибольшим количеством проданных товаров: {max_categ}")

total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases, 1.0)
average_price_by_category(purchases)
most_frequent_category(purchases)