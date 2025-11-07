# WebTravel ✈️

A Django-based web application for a fictional travel agency, allowing users to browse, book, and manage travel packages.

## ✨ Features

*   **User Authentication:** Secure user registration, login, and logout functionality.
*   **User Roles:** Distinction between regular clients and staff members with different levels of access and permissions.
*   **Profile Management:** Users can view and update their profile information, including their profile picture.
*   **Trip Management (Staff):** Staff members can create, read, update, and delete travel packages (CRUD).
*   **City Management (Staff):** Staff can manage the list of available cities for the trips.
*   **Stage Management (Staff):** Staff can add, modify, and remove stages (cities) within a trip.
*   **Image Uploads:** Support for uploading images for travel packages and user profiles.
*   **Dynamic Menus:** The navigation menu changes based on the user's authentication status and role.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   [Python 3.10+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads/)

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/YoussefAB555/R5A05---Programmation-avanc-e-Cat-gorie-R-f-rentiels-de-comp-tences.git
    cd R5A05---Programmation-avanc-e-Cat-gorie-R-f-rentiels-de-comp-tences
    ```

2.  **Run the setup script:**

    Open a PowerShell terminal and run the following command:

    ```powershell
    .\run_project.ps1
    ```

    This script will automatically:
    *   Create a Python virtual environment (`.venv`).
    *   Install all the required dependencies from `requirements.txt`.
    *   Start the Django development server.

## 🛠️ Usage

Once the server is running, you can access the application in your web browser at:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

To access the admin panel, you will need to create a superuser:

```sh
.venv\Scripts\python.exe webtravel\manage.py createsuperuser
```

Then, you can access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## 💻 Technologies

*   **Backend:**
    *   [Python](https://www.python.org/)
    *   [Django](https://www.djangoproject.com/)
*   **Frontend:**
    *   HTML5
    *   CSS3
    *   [Bootstrap 5](https://getbootstrap.com/)
*   **Database:**
    *   [SQLite](https://www.sqlite.org/index.html) (for development)

## 📁 Project Structure

```
.R5A05---Programmation-avanc-e-Cat-gorie-R-f-rentiels-de-comp-tences/
├── .venv/                  # Virtual environment
├── webtravel/                # Django project folder
│   ├── applitravel/          # Django app for travel management
│   ├── applicompte/          # Django app for user account management
│   ├── webtravel/            # Project settings
│   ├── manage.py             # Django's command-line utility
│   └── requirements.txt      # Project dependencies
├── run_project.ps1           # PowerShell script for setup and execution
└── README.md                 # This file
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
