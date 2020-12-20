
class Recipe:

    def __init__(self, id_no, name, ingredients, prep_time, cook_time, total_time, servings, cuisine, course, diet, instructions, URL):

        self._id_no = id_no
        self._name = name
        self._ingredients = ingredients
        self._prep_time = prep_time
        self._cook_time = cook_time
        self._total_time = total_time
        self._servings = servings
        self._cuisine = cuisine
        self._course = course
        self._diet = diet
        self._instructions = instructions
        self._url = URL

    
    def __str__(self):

        return f'Recipe: {self._name} || Ingredients: {self._ingredients} | Instructions: {self._instructions}'

    def id_no(self):
        
        return self._id_no
    
    
    def name(self):
        
        return self._name
    
    
    def ingredients(self):
        
        return self._ingredients
    
    
    def prep_time(self):
        
        return self._prep_time
    
    
    def cook_time(self):
        
        return self._cook_time
    
    
    def total_time(self):
        
        return self._total_time
    
    
    def servings(self):
        
        return self._servings
    
    
    def cuisine(self):
        
        return self._cuisine
    
    
    def course(self):
        
        return self._course
    
    
    def diet(self):
        
        return self._diet
    
    
    def instructions(self):
        
        return self._instructions

    
    def url(self):
        
        return self._url


    def __lt__(self, other):
        
        return self._total_time < other.total_time()

    
    def __le__(self, other):
        
        return self._total_time <= other.total_time()

    
    def __gt__(self, other):
        
        return self._total_time > other.total_time()
    
    
    def __ge__(self, other):
        
        return self._total_time >= other.total_time()
    
    
    def __eq__(self, other):
        
        return self._total_time == other.total_time()
    

    def __ne__(self, other):
        
        return self._total_time != other.total_time()


    
        
