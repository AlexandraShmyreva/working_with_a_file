def recipes(file_name):
    with open(file_name, encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            well = line[:-1]
            ingredient_list = []
            res = int(file.readline().strip())
            for result in range(res):
                ingredients = file.readline().strip().split('|')
                ingredient_dict = {}
                for indredient in ingredients:
                    ingredient_dict['ingredient_name'] = ingredients[0]
                    ingredient_dict['quantity'] = ingredients[1]
                    ingredient_dict['measure'] = ingredients[2]
                ingredient_list.append(ingredient_dict)
                cook_book[well] = ingredient_list
            file.readline()
        return cook_book

print(recipes('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    menu = recipes('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in menu[dish]:
            ingredient_dict = dict([(ingredient['ingredient_name'], {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count})])
            shop_list.update(ingredient_dict)
    return shop_list

print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))
