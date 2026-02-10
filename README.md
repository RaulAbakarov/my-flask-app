# 🐍 Flask Web Application

A Python Flask application with PostgreSQL database integration, deployed on Vercel. Features user authentication and data management capabilities.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

## 🔗 Live Demo

**[Visit App →](https://my-flask-app-navy.vercel.app/)**

## ✨ Features

- 🔐 **User Authentication** — Login system with form handling
- 🗄️ **PostgreSQL Database** — Neon serverless Postgres integration
- 📊 **Data Viewing** — Admin view for stored data
- 🚀 **Serverless Deployment** — Vercel serverless functions
- 📱 **Responsive Templates** — HTML templates with Jinja2

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend | Flask |
| Database | PostgreSQL (Neon) |
| DB Driver | pg8000 |
| Deployment | Vercel |
| Templates | Jinja2 |

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL database (or Neon account)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RaulAbakarov/my-flask-app.git
   cd my-flask-app
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your database and update `DATABASE_URL` in `app.py`

5. Run the application:
   ```bash
   python app.py
   ```

## 🏗️ Project Structure

```
my-flask-app/
├── app.py              # Main Flask application
├── templates/
│   ├── index.html      # Landing page
│   └── view_data.html  # Data display page
├── requirements.txt    # Python dependencies
├── setup.py            # Package setup
├── Procfile            # Process file for deployment
└── vercel.json         # Vercel configuration
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Landing page |
| POST | `/login` | User authentication |
| GET | `/view-data` | View stored data |

## 📦 Dependencies

```
Flask
pg8000
gunicorn
```

## 🚀 Deployment

### Vercel Deployment

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

The `vercel.json` is pre-configured for Python serverless functions.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Raul Abakarov** — [GitHub](https://github.com/RaulAbakarov) | [LinkedIn](https://linkedin.com/in/raulabakarov)
