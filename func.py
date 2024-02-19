def outer_function():
    name="sourav"
    
    def inner_function(name):
        
        print(name)
        name="Mohanta"
        return name

    name =inner_function(name) 
    print(name) 

outer_function()