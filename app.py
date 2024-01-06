import os
from openai import OpenAI
from flask import Flask, render_template, request
from dotenv import find_dotenv, load_dotenv

app = Flask(__name__, static_url_path='/static')

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input1 = request.form['diet']
        input2 = request.form['recipe_level']
        input3 = request.form['cook_time']
        input4 = request.form['serving_size']
        input5 = request.form['ingredients']
        input6 = request.form['cuisine']
        input7 = request.form['allergies']
        prompt = "I have the following ingredients: " + input5 + ". Please give me a " + input2 + " " + input1 + " " + input6 + " recipe that will serve " + input4 + " people and will take " + input3 + " to cook. The recipe does not need to use all ingredients. The recipe generated should be separated out into the following titles: 'Dish:', 'Ingredients:', 'Instructions:' and 'Notes:' The recipe should be written in a way that is easy to follow."

        if(input7 != ""):
            prompt += "I have the following allergies: " + input7 + "."

        client = OpenAI(api_key=OPEN_AI_API_KEY)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}])

        recipe = completion.choices[0].message.content

        dish_pointer = recipe.find("Dish:")
        ingredients_pointer = recipe.find("Ingredients:")
        instructions_pointer = recipe.find("Instructions:")
        notes_pointer = recipe.find("Notes:")

        dish = recipe[dish_pointer+6:ingredients_pointer-1]
        ingredients = recipe[ingredients_pointer+13:instructions_pointer-1]
        instructions = recipe[instructions_pointer+14:notes_pointer-2]
        notes = recipe[notes_pointer+7:]

        while(instructions.find("\n\n") != -1):
            instructions = instructions.replace("\n\n", "\n")

        
        def get_dynamic_image_url():
            response = client.images.generate(
                model="dall-e-3",
                prompt="I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: bird's eye view of " + dish + " on a kitchen counter, but ONLY the dish. Make it realistic.",
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            return image_url
        
        dynamic_image_url = get_dynamic_image_url()
        
        return render_template('result.html', dish=dish, ingredients=ingredients, instructions=instructions, notes=notes, serving_size=input4, cook_time=input3, dynamic_image_url=dynamic_image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




'''
allergies = input("Do you have any allergies? (separate each allergy with a comma) ")
'''