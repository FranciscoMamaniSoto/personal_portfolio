from flask import Flask, render_template, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Helper function to load data from JSON files
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return []

# Add current date to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Routes
@app.route('/')
def index():
    projects = load_data('data/projects.json')
    articles = load_data('data/articles.json')
    return render_template('index.html', projects=projects, articles=articles)

@app.route('/portfolio')
def portfolio():
    projects = load_data('data/projects.json')
    return render_template('portfolio.html', projects=projects)

@app.route('/articles')
def articles():
    articles = load_data('data/articles.json')
    return render_template('articles.html', articles=articles)

@app.route('/article/<article_id>')
def article(article_id):
    articles = load_data('data/articles.json')
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return "Article not found", 404

@app.route('/project/<project_id>')
def project(project_id):
    projects = load_data('data/projects.json')
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    return "Project not found", 404

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Create sample data files if they don't exist
    if not os.path.exists('data/projects.json'):
        sample_projects = [
            {
                "id": "project1",
                "title": "Machine Learning Project",
                "description": "A project using machine learning to predict user behavior based on historical data. This project implements several classification algorithms and compares their performance.",
                "image": "project1.jpg",
                "technologies": ["Python", "TensorFlow", "Scikit-learn"],
                "github_url": "https://github.com/yourusername/project1",
                "date": "2023-01-15"
            },
            {
                "id": "project2",
                "title": "Data Analysis Dashboard",
                "description": "Interactive dashboard for analyzing sales data and visualizing trends. Built with Python and Plotly Dash, this tool helps stakeholders make data-driven decisions.",
                "image": "project2.jpg",
                "technologies": ["Python", "Pandas", "Plotly"],
                "github_url": "https://github.com/yourusername/project2",
                "date": "2023-03-20"
            }
        ]
        with open('data/projects.json', 'w') as f:
            json.dump(sample_projects, f, indent=2)
    
    if not os.path.exists('data/articles.json'):
        sample_articles = [
            {
                "id": "article1",
                "title": "Introduction to Machine Learning",
                "content": "Machine learning is a field of study that gives computers the ability to learn without being explicitly programmed. It focuses on developing computer programs that can access data and use it to learn for themselves.\n\nThe process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples we provide. The primary aim is to allow computers to learn automatically without human intervention or assistance and adjust actions accordingly.\n\nMachine learning algorithms are often categorized as supervised, unsupervised, and reinforcement learning...",
                "image": "article1.jpg",
                "tags": ["Machine Learning", "AI", "Tutorial"],
                "date": "2023-02-10"
            },
            {
                "id": "article2",
                "title": "Data Visualization Best Practices",
                "content": "When creating data visualizations, it's important to follow certain best practices to ensure your graphics effectively communicate the intended information.\n\nFirst, always start with a clear purpose. Before creating any visualization, ask yourself what specific question you're trying to answer or what insight you want to convey.\n\nSecond, choose the right type of visualization for your data. Bar charts are great for comparing values across categories, line charts show trends over time, and scatter plots reveal relationships between variables.\n\nThird, keep it simple. Avoid cluttering your visualizations with unnecessary elements like excessive gridlines, decorative graphics, or 3D effects that don't add value...",
                "image": "article2.jpg",
                "tags": ["Data Visualization", "Best Practices"],
                "date": "2023-04-05"
            }
        ]
        with open('data/articles.json', 'w') as f:
            json.dump(sample_articles, f, indent=2)
    
    app.run(debug=True)
