recipe = "Dish: Vegan Chickpea Curry with Rice Ingredients: - 2 large carrots, peeled and diced - 2 medium potatoes, peeled and diced - 1 can chickpeas, drained and rinsed - 1 cup basmati rice - 1 onion, chopped - 3 cloves garlic, minced - 1 red bell pepper, diced - 1 cup coconut milk - 2 tablespoons tomato paste - 2 tablespoons curry powder - 1 teaspoon turmeric powder - 1 teaspoon cumin powder - 1 teaspoon paprika - Fresh cilantro, for garnish - Salt and pepper, to taste - Olive oil, for cooking Instructions: 1. Heat a large pot over medium heat and add olive oil. Add the chopped onion and minced garlic, cooking until they become translucent and fragrant. 2. Add the diced carrots and potatoes to the pot, stirring well to coat them with the onion and garlic mixture. Cook for about 5 minutes, until they start to soften. 3. In a small bowl, mix together the curry powder, turmeric powder, cumin powder, and paprika. Add this spice mixture to the pot, stirring until the vegetables are evenly coated. 4. Stir in the tomato paste and red bell pepper, allowing all the flavors to combine. Cook for another 2 minutes. 5. Add the drained chickpeas and coconut milk to the pot, stirring well. Season with salt and pepper to taste. 6. Bring the mixture to a boil, then reduce the heat to low. Cover the pot and allow the curry to simmer for 45 minutes, or until the carrots and potatoes are tender. 7. While the curry is simmering, prepare the rice according to package instructions. 8. Once the curry is cooked, adjust the seasoning if needed. Serve the vegan chickpea curry over cooked basmati rice, garnished with fresh cilantro. Notes: - Feel free to add other vegetables such as green beans or peas to the curry for added variety. - If you prefer a spicier curry, add a pinch of cayenne pepper or chili flakes. - Leftovers can be stored in an airtight container in the refrigerator for up to 3 days."

dish_pointer = recipe.find("Dish:")
ingredients_pointer = recipe.find("Ingredients:")
instructions_pointer = recipe.find("Instructions:")
notes_pointer = recipe.find("Notes:")

dish = recipe[dish_pointer+6:ingredients_pointer]
ingredients = recipe[ingredients_pointer+13:instructions_pointer]
instructions = recipe[instructions_pointer+14:notes_pointer]
notes = recipe[notes_pointer+7:]
