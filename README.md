# Undergrad Academic Report

This Flask-based web application displays student academic reports by fetching data from MongoDB. It calculates the GPA and CGPA for semesters and displays the information in a user-friendly format.

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6+
- You have installed MongoDB
- You have created a MongoDB database and a collection named `test`
- You have a MongoDB connection string for your database

### Installation and Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/khushaalan/UndergradAcademicReport.git
    ```

2. Navigate to the project directory:

    ```bash
    cd UndergradAcademicReport
    ```

3. Create a `.env` file in the root directory and add your MongoDB connection string like so:

    ```env
    MONGO_CONNECTION_STRING="your_mongodb_connection_string"
    ```

4. Install the necessary Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    python runserver.py
    ```

The application should now be running at `localhost:8000`.

## Contributing

We welcome contributions to this project, please fork this repository and create a pull request if you have something you want to add or improve.

## Contact Developer

If you want to contact the developer, you can reach out at:
- Khushaalan Arjunan - khushaalanarjunan@gmail.com
