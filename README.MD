# Bank security console

[Russian](RU_README.MD)

## Description

This is an internal repository for Siyanie Bank employees. If you got into this repository by accident, you will not be able to launch it, because... you do not have access to the database, but you can freely use the layout code or see how queries to the database are implemented.

The security console is a website that can be connected to a remote database with visits and pass cards of our bank employees

## Installation

To install this project, you will need Python and Django installed on your machine. You can then clone this repository and install the required dependencies with:

```bash
pip install -r requirements.txt
```
## Setting up the environment

Before starting the program, you must set the following environment variables:

- `DB_ENGINE`: Database connection string.
- `DB_HOST`: Database host.
- `DB_PORT`: The port your database is running on.
- `DB_NAME`: Database name.
- `DB_USER`: Database user name.
- `DB_PASSWORD`: Database user password.
- `SECRET_KEY`: Django secret key. This key is used to provide a cryptographic signature and must be unique and difficult to guess.
- `DEBUG`: Debugging mode. Set to `'True'` to enable debug mode. Important: do not use debug mode in production!
- `ALLOWED_HOSTS`: List of hosts that are allowed to serve your Django application. Hosts must be listed separated by commas. Example: `'localhost,127.0.0.1'`.

## Usage

To run this project, go to the project directory and run the following command:

```bash
python manage.py runserver 0.0.0.0:8000
```

This will start the Django development server at 0.0.0.0:8000.

To access the web application, open your browser and enter the following web address: http://127.0.0.1:8000/.

##Models

The project has two main models:

- **Passcard**: Represents a pass card with fields for activity status, creation time, password and owner name.

- **Visit**: Represents a visit with fields for creation time, associated pass card, entry time, and exit time. It also includes methods for calculating the duration of a visit and checking whether the visit is long.

## Representation

The project includes several presentations:

- **storage_information_view**: Displays information about current visits.

- **passcard_info_view**: Displays information about visits to a specific pass card.

- **active_passcards_view**: Displays all active passcards.

## License

This project is licensed under the MIT License.

## Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).
