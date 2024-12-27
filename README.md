# Mental Fatigue Score Checker

This is a simple web application to check your mental fatigue score based on a questionnaire. The application is built using Python and Streamlit.

## Features

- Asks a series of questions to assess mental fatigue.
- Calculates a mental fatigue score between 0.0 and 10.0.
- Provides feedback based on the calculated score.

## Installation

1. Clone the repository or download the code.
2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
3. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501`.
3. Answer the questions using the dropdown menus.
4. Click on the "Submit" button to see your mental fatigue score and feedback.

## Explanation

- **Questions**: The app asks a series of questions to assess mental fatigue.
- **Score Calculation**: The app calculates a mental fatigue score based on the user's responses.
- **Feedback**: The app provides feedback based on the calculated score.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
