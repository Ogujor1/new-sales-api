# Sales API

A Django REST Framework API for managing blog posts, authors, features, projects, and about information.

## Features

- **Post Management**: Create and manage blog posts with slug-based URLs
- **Author Management**: Manage authors with profile pictures
- **Features**: Showcase features or services with external links
- **Projects**: Display portfolio projects with thumbnails
- **About**: Manage company/personal information with mission statements

## Models

### Post App
- **Author**: Represents authors with full name, description, and thumbnail
- **Post**: Blog posts with title, slug, description, and author relationship

### Profiles App
- **Feature**: Services/features with name, title, URL, and timestamp
- **Project**: Portfolio projects with title, description, and thumbnail
- **About**: About information with title, description, mission, and thumbnail

## API Endpoints

All endpoints are prefixed with `/api/`

### Authors
- `GET /api/authors/` - List all authors
- `POST /api/authors/` - Create a new author
- `GET /api/authors/{id}/` - Retrieve a specific author
- `PUT/PATCH /api/authors/{id}/` - Update an author
- `DELETE /api/authors/{id}/` - Delete an author

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a new post
- `GET /api/posts/{slug}/` - Retrieve a specific post by slug
- `PUT/PATCH /api/posts/{slug}/` - Update a post
- `DELETE /api/posts/{slug}/` - Delete a post

### Features
- `GET /api/features/` - List all features
- `POST /api/features/` - Create a new feature
- `GET /api/features/{id}/` - Retrieve a specific feature
- `PUT/PATCH /api/features/{id}/` - Update a feature
- `DELETE /api/features/{id}/` - Delete a feature

### Projects
- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create a new project
- `GET /api/projects/{id}/` - Retrieve a specific project
- `PUT/PATCH /api/projects/{id}/` - Update a project
- `DELETE /api/projects/{id}/` - Delete a project

### About
- `GET /api/about/` - List all about entries
- `POST /api/about/` - Create a new about entry
- `GET /api/about/{id}/` - Retrieve a specific about entry
- `PUT/PATCH /api/about/{id}/` - Update an about entry
- `DELETE /api/about/{id}/` - Delete an about entry

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sales_api_claude_code
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Technologies Used

- Django 5.0.7
- Django REST Framework 3.15.2
- Pillow 10.4.0 (for image handling)
- SQLite (default database)

## Project Structure

```
sales_api_claude_code/
├── sales_api/          # Main project settings
├── post/               # Post and Author models
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── profiles/           # Features, Projects, and About models
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── media/              # Uploaded media files
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.
