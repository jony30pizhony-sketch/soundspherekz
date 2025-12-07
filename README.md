# SoundSphereKZ

SoundSphereKZ is a Django-based web application.

## Prerequisites

- Python 3.x
- pip

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd soundspherekz
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    # Windows
    .\env\Scripts\activate
    # Linux/Mac
    source env/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6.  **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

-   `mafony/`: Main application app.
-   `soundphereProject/`: Project configuration settings.
-   `templates/`: HTML templates.
-   `static/`: Static files (CSS, JS, images).
-   `users/`: User management app.

