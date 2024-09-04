**Flask Number Guessing Game**
A simple web application built with Flask that implements a number guessing game. Users can guess a number within a specified range, and the application provides feedback on whether the guess was too high, too low, or correct.

**Features**

-> Input fields are used to set the lower and upper bounds of the number range.

-> Input field for entering the guess.

-> Feedback on the guess compared to the randomly generated number.

**Technologies Used**
Python: A programming language for developing the application.
Flask: Web framework used to create the web server.
HTML: Markup language used for creating the web interface.
Math Module: Used for calculating the number of guesses.

**Setup Instructions**
Clone the Repository

    git clone https://github.com/KarthikVolisetty/flask-number-guessing-game.git
    
    cd flask-number-guessing-game
    
Create and Activate a Conda Environment (Optional)

    conda create -n guessing-game python=3.8
    
    conda activate guessing-game

**Install Dependencies**
Make sure Flask is installed. You can install it using pip:

    pip install flask

**Run the Application**
-> Open Anaconda Prompt or your terminal.

-> Navigate to the project directory.

**Run the Flask application:**
    
    python app.py
    
-> Open a web browser and go to http://127.0.0.1:5000/ to view the application.

**Project Structure**
app.py: Main Flask application script.
templates/: Directory containing HTML templates.
index.html: HTML file for the user interface.

**Code Explanation**
app.py: Contains the Flask application logic. It handles HTTP requests, processes user input, generates a random number, and provides feedback based on the user’s guess.
index.html: HTML template that provides the user interface for the number guessing game. It includes a form for inputting the bounds, and guesses and displays feedback from the server.

**Contributing**
Please feel free to fix the repository and submit pull requests. For major changes or enhancements, please open an issue to discuss the changes before submitting a pull request.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or further information, please contact karthikvolisetty@gmail.com or open an issue on the GitHub repository.
