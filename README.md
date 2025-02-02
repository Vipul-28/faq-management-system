# FAQ Management System

This is a Django-based FAQ Management System that allows users to manage Frequently Asked Questions (FAQs). It supports multi-language translations, uses a WYSIWYG editor for the answers, and provides a REST API for interacting with FAQs. This system also integrates caching with Redis to improve performance.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Virtual Environment](#set-up-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Redis](#set-up-redis)
  - [Database Migration](#database-migration)
  - [Create Superuser](#create-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Usage](#usage)
  - [API Usage](#api-usage)
  - [Managing FAQs via Admin](#managing-faqs-via-admin)
- [Contribution Guidelines](#contribution-guidelines)

## Features

- **FAQ Management**: Create, read, update, and delete FAQs through both API and Admin.
- **WYSIWYG Editor**: Allows formatting the answers using `django-ckeditor`.
- **Multi-Language Support**: Retrieve FAQs in different languages (e.g., English, Hindi, Bengali).
- **Caching**: Uses Redis to cache translations for faster API responses.
- **API Support**: Access FAQs in multiple languages by passing the `lang` query parameter.
- **Admin Interface**: A user-friendly Django Admin interface to manage FAQs.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.x
- Django 5.x
- Redis (for caching)
- `django-ckeditor` (for WYSIWYG editor support)
- `googletrans` (for language translation)

## Installation

Follow the steps below to get the project running on your local machine.

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Vipul-28/faq-management-system
```

### Set Up Virtual Environment

To isolate the project dependencies, set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### Set Up Redis

Make sure Redis is installed and running. You can install Redis locally or use a hosted Redis service. To install Redis locally:

For Ubuntu:

```bash
sudo apt install redis-server
redis-server
```

### Database Migration

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### Create Superuser (Optional)

If you wish to access the Django Admin interface, create a superuser account:

```bash
python manage.py createsuperuser
```

### Run the Development Server

Start the development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

### API Usage

The system provides a REST API to manage FAQs and retrieve them in multiple languages.

#### Fetch FAQs in English (default)

```bash
curl http://localhost:8000/api/faqs/
```

#### Fetch FAQs in Hindi

```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

#### Fetch FAQs in Bengali

```bash
curl http://localhost:8000/api/faqs/?lang=bn
```

### Managing FAQs via Admin

You can manage FAQs via the Django Admin interface:

1. Go to `http://127.0.0.1:8000/admin/`.
2. Log in using the superuser credentials you created earlier.
3. In the **FAQ** section, you can add, update, or delete FAQs.
4. FAQs will be shown with their translations in different languages.

