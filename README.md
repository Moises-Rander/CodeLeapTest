# CodeLeap Backend Application Test

This is a backend API project built with Django and Django REST Framework (DRF). It provides authentication for users and allows them to manage posts in a CRUD (Create, Read, Update, Delete) system. The application is hosted on AWS and uses PostgreSQL as the database.
Link to the working version of the project: http://52.71.206.213/api/v1/posts/ or http://52.71.206.213/api/v1/posts/1

## Features

- **Post Management**: Fully functional CRUD operations for posts, including creating, reading, updating, and deleting posts. Each post has a title, content, creation date, and is associated with the user who created it.
  
## Technologies Used

- **Django**: Web framework for building the API.
- **Django REST Framework (DRF)**: For creating the RESTful API endpoints.
- **PostgreSQL**: Relational database used for data storage.
- **AWS EC2**: For hosting the application with an Elastic IP.

## Pre-requisites

To run the project locally, you will need:

- Python
- PostgreSQL
- Pip (Python package manager)
- Git
- An AWS account (if deploying)

## Installation

Follow these steps to set up the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/codeleap-backend.git
cd CodeLeapTest
```
### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database
Ensure PostgreSQL is installed and running. Create a database for the project and configure your environment variables using ```python-dotenv```.  
* Example ```.env``` file:
    ```env
    DATABASE_PASSWORD=your_secret_key
    ```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Your application will be available at http://127.0.0.1:8000.

## API Endpoints

The API provides the following CRUD endpoints for posts:

### 1. Create Post

• POST/posts/: Create new post.

Request body example:

```json
{
  "title": "New Post",
  "content": "Content of the new post"
}
```
Response:
```json
{
  "id": 2,
  "title": "New Post",
  "content": "Content of the new post",
  "created_at": "2025-01-08T12:00:00Z",
  "user": 1
}
```
### 2. List Posts

• GET/posts/: Retrieves all posts.

Response example:
```json
[
  {
    "id": 1,
    "title": "My First Post",
    "content": "Content of the post",
    "created_at": "2025-01-01T12:00:00Z",
    "user": 1
  }
]
```

### 3. Retrieve single Post

• GET/posts/int:pk/: Retrieves a single post by its ID.

Response example:
```json
{
  "id": 1,
  "title": "My First Post",
  "content": "Content of the post",
  "created_at": "2025-01-01T12:00:00Z",
  "user": 1
}
```


### 4. Update Post

• PUT /posts/int:pk/: Update an existing post.

Response body example:
```json
{
  "title": "Updated Post",
  "content": "Updated content"
}
```

### 5. Partial Update Post

• PATCH /posts/int:pk/: Partially update a post (for example, just the title or content).

Response body example:
```json
{
  "title": "Partially Updated Post"
}
```
### 6. Delete post

• DELETE /posts/int:pk/: Delete a post.

## Environmental Variables

The project uses environment variables for sensitive information and configuration. You can configure the following in your ```.env``` file:

• ```DATABASE_URL```: The URL for the PostgreSQL database (e.g., ```postgres://username:password@localhost:5432/database_name)```.
• ```SECRET_KEY```: Django's secret key.
• ```DEBUG```: Set to ```True``` for development and ```False``` for production.
• ```ALLOWED_HOSTS```: Hosts that are allowed to connect to the Django application (e.g., ```localhost,127.0.0.1```).

## Deployment on AWS
The application is hosted on AWS using EC2 with an Elastic IP.
Follow these steps for deployment:

1. Set up an Amazon EC2 instance and configure it to run a Django application.
2. Install PostgreSQL on the EC2 instance, or use Amazon RDS for a managed PostgreSQL service.
3. Configure the environment variables on AWS for production.
4. Point your domain (if applicable) to the Elastic IP.

## Screenshots
1. Admin page to manage the project tables
   ![Captura de Tela 2025-01-08 às 04 39 51](https://github.com/user-attachments/assets/5cf98552-8054-4dc3-8066-cae951d94bb4)
2. /posts/ page
   ![Captura de Tela 2025-01-08 às 04 40 33](https://github.com/user-attachments/assets/442a6ede-de26-48f0-9ff7-7e89b76858e7)
3. /posts/int:pk/ page
   ![Captura de Tela 2025-01-08 às 04 41 01](https://github.com/user-attachments/assets/36e923ef-5b0b-49cf-a38f-bb95c11e4b00)
