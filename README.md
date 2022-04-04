# TASK: Problem 2 (Guess the number):
* Use Python or Java for following REST API code
* User selects an integer number in their mind between 1 - 100.
    * The number is never input inside the system anywhere directly.
* Computer tries to guess the selected number with multiple attempts with API calls.
* At each attempt the computer guesses a number and shows it to the user.
* User can give feedback in one of the four options
    * Start (Input is given to start the game again)
    * Greater than (>) (If guessed number is greater than his selected number) ○ Less than (<) (If guessed number is less than his selected number)
    * Equal (=) (If guessed number is equals to his selected number)
* **Important: Computer should be able to guess the correct number in less than or equal to 7 attempts always. (Start action should be counted in attempt)**
* Create following api
    * Start game
        * Input
        ```
        {
            "action": "start"
        }
        ```
        * Output
        ```
        {
            "guessed_number": 10,
            "attempt": 1,
        }
        ```
    * Greater Than
        * Input
        ```
        {
            "action": ">"
        }
        ```
        * Output
        ```
        {
            "guessed_number": 4,
            "attempt": 2,
        }
        ```
    * Less Than
        * Input
        ```
        {
            "action": "<"
        }
        ```
        * Output
        ```
        {
            "guessed_number": 4,
            "attempt": 2,
        }
        ```
    * Equal To
        * Input
        ```
        {
            "action": "="
        }
        ```
        * Output
        ```
        {
            "guessed_number": "Number is predicted successfully! Your selected number is 6",
            "attempt": 6,
        }
        ```
* Write Unit tests.
* Use redis.
* Use dockerized backend workers.