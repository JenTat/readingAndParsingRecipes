
import recipe_class as r
import csv



def read_file(filename):

    recipe_dictionary = {}

    with open(filename, encoding='utf-8', errors='ignore') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            ingredients_list = line["TranslatedIngredients"].split(",")
            ingredients_list = [i.strip() for i in ingredients_list]
            
            srno = int(line['\ufeffSrno'])
            prepTime = int(line['PrepTimeInMins'])
            cookTime = int(line['CookTimeInMins'])
            totalTime = int(line['TotalTimeInMins'])
            servings = int(line['Servings'])
            cuisine = line['Cuisine']
            course = line['Course']
                
            recipe = r.Recipe(srno, line['TranslatedRecipeName'], ingredients_list, prepTime,
                              cookTime, totalTime, servings, cuisine, course,
                              line['Diet'], line['TranslatedInstructions'], line['URL'])

            if cuisine not in recipe_dictionary:
                recipe_dictionary[cuisine] = {}

            if course not in recipe_dictionary[cuisine]:
                recipe_dictionary[cuisine][course] = []

            recipe_dictionary[cuisine][course].append(recipe)

    return recipe_dictionary     



def generate_index_file(dataset, filename):
    
    with open(filename, "w", encoding='utf-8', newline="", errors='ignore') as recipesOut:

        writer = csv.writer(recipesOut)

        titles = ['ID','Cuisine','Course','Diet','Name','Total Time (prep & cook)','Servings']

        line = titles
        writer.writerow(line)
        
        for cuisine in dataset:

            for course in dataset[cuisine]:

                for recipe in dataset[cuisine][course]:
                    
                    line = [recipe.id_no(), cuisine, course, recipe.diet(), recipe.name(), recipe.total_time(), recipe.servings()]

                    writer.writerow(line)


    
def generate_recipe_detail_file(dataset, filename):
    
    with open(filename, "w", encoding='utf-8', errors='ignore') as recipesOut:

        for cuisine in dataset:
            for course in dataset[cuisine]:
            
                for recipe in dataset[cuisine][course]:

                    s = ""
                    s += f'{recipe.id_no()}\n'
                    s += f'{recipe.name()}\n'
                    s += f'prep time: {recipe.prep_time()} min | cook_time: {recipe.cook_time()} min | total_time: {recipe.total_time()} min\n'
                    s += f'{cuisine} | {course} | {recipe.diet()}\n'
                    s += f'Makes {recipe.servings()} servings\n' 
                    s += f'{recipe.url()}\n'
                    s += f'\n'
                    s += f'Ingredients\n'
                    ingredients = recipe.ingredients()
                    for i in ingredients:
                            s += f'{i}\n'
                    s += f'\n'
                    s += f'Instructions\n'
                    s += f'{recipe.instructions()}\n'
                    s += f'\n'

                    recipesOut.write(s)


#MAIN
dataset = read_file("IndianFood.csv")

generate_index_file(dataset, "Indian_Food_Recipe_Index.csv")

generate_recipe_detail_file(dataset, "Indian_Food_Recipe_Cards.txt")
