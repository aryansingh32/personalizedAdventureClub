<h1 align="left">Welcome to the Personalized Adventure Club!</h1>
<p align="left">An interactive Python program that helps you plan a custom adventure trip based on your preferences. Whether you're planning a luxurious getaway or a modest trip, this program helps you make informed decisions.</p>
<h2 align="left">Features</h2>
<p align="left"> - ✨ Welcome Message: Enter your name and get a personalized welcome message.<br> - 🌍 Destination Choice: Choose between a mountain or beach adventure.<br> - 💸 Budget Classification: Classifies your trip as luxurious, solid, or modest based on your daily budget.<br> - 📅 Trip Duration: Specify the number of days you'd like your trip to last.<br> - 📊 Cost Estimation: Calculates the total estimated cost for the trip based on your budget and duration.<br> - 🎉 Final Trip Summary: Provides a neat summary of your destination, duration, and total cost.<br> </p>
<h2 align="left">How It Works</h2>
<p align="left"> 1. Input your name for a personalized greeting.<br> 2. Choose your destination: Mountain or Beach.<br> 3. Enter your daily budget, and the program will classify your trip.<br> 4. Specify the number of travel days.<br> 5. Receive a personalized adventure plan with total cost and trip summary.<br> </p>
<h2 align="left">Requirements</h2>
<p align="left"> - 🐍 Python 3.x: Ensure you have Python installed on your system to run the program. </p>
<h2 align="left">Usage</h2>
<p align="left"> 1. Clone or download the script.<br> 2. Open your terminal or command prompt.<br> 3. Run the script using Python:<br>


```bash
python adventure.py
```
Follow the on-screen prompts to enter your name, choose your destination, input your budget, and specify the number of travel days.
</p>
<h2 align="left">Code Structure</h2>
<p align="left"> 1.<b> getValidInput(prompt) </b>: A helper function to take valid integer input from the user.<br>2. <b>budgetHandling() </b>:  Prompts the user to enter their daily budget.<br>3.<b> daysHandling() </b>: Prompts the user to enter how many days they want to travel.<br>4.<b> dailyBudget(budget) </b>: Classifies the budget into luxury, solid, or modest.<br>5.<b> destination() </b>: Asks the user to choose between a mountain or beach destination.<br>6.<b> welcomeMsg() </b>: Greets the user with a personalized welcome message.<br>7.<b> main() </b>: Orchestrates the entire process, calling the relevant functions and providing the final trip summary.<br> </p>
<h2 align="left">Example Interaction</h2>



```bash

Let's create a personalized adventure plan for you!
Welcome to the Personalized Adventure Club! May I have your name, please? John

Hello, John! We're excited to have you on a journey with us!

Where would you like to explore? Please choose between 'mountain' or 'beach': mountain
Great choice! You've selected the mountain as your adventure destination.

To help us plan your adventure, could you share your daily budget? 300
That's a solid budget! You’ll have a comfortable and enjoyable experience.

How many days would you like your adventure to last? 3

Your adventure plan is all set, John!
Destination: Mountain
Duration: 3 day(s)
Estimated total cost: $900
We hope you have an amazing journey ahead!

Thank you for choosing the Personalized Adventure Club!
```

<h2 align="left">Customization</h2>
<p align="left">Feel free to modify the code to add more destinations, budget classifications, or other features. The framework is flexible and can be extended for more complex adventure planning.</p>
<h2 align="left">License</h2>
<p align="left">This project is open source and available for modification.</p>
