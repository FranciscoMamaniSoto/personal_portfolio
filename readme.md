# Personal Portfolio Website

A minimalistic, clean personal portfolio website built with Python and Flask. This portfolio showcases machine learning and data analysis projects, as well as articles on related topics.

## Features

- Clean, minimalistic design inspired by Dario Amodei's website
- Separate pages for portfolio/projects and articles
- Responsive design that works on all devices
- Easy to update and maintain with JSON data files
- Built with Python and Flask

## Project Structure

```
portfolio-website/
├── app.py                    # Main Flask application
├── requirements.txt          # Dependencies
├── static/                   # Static files
│   ├── css/
│   │   └── style.css         # Custom CSS
│   ├── js/
│   │   └── main.js           # Custom JavaScript
│   └── images/               # Images folder (create this)
├── templates/                # HTML templates
│   ├── base.html             # Base template with common elements
│   ├── index.html            # Home page
│   ├── portfolio.html        # Portfolio/Projects page
│   ├── articles.html         # Articles page
│   ├── article.html          # Individual article template
│   └── project.html          # Individual project template
└── data/                     # Data storage (created automatically)
    ├── projects.json         # Project data 
    └── articles.json         # Article data
```

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- Git

### macOS Setup Instructions

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/portfolio-website.git
cd portfolio-website
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create the images directory:

```bash
mkdir -p static/images
```

5. Run the Flask application:

```bash
python app.py
```

6. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

## GitHub Repository Setup

1. Create a new repository on GitHub.

2. Initialize your local directory as a Git repository (if not already done):

```bash
git init
```

3. Add your files to the Git repository:

```bash
git add .
git commit -m "Initial commit"
```

4. Connect your local repository to your GitHub repository:

```bash
git remote add origin https://github.com/yourusername/portfolio-website.git
git branch -M main
git push -u origin main
```

## Customization

### Personal Information

Edit the HTML templates in the `templates` folder to update your personal information:
- Change "Your Name" in `base.html` and `index.html`
- Update social links in `base.html`
- Modify the about section in `index.html`

### Projects

Update the `data/projects.json` file to add your own projects. Each project should follow this format:

```json
{
  "id": "unique-project-id",
  "title": "Project Title",
  "description": "Project description...",
  "image": "project-image.jpg",
  "technologies": ["Python", "TensorFlow", "Scikit-learn"],
  "github_url": "https://github.com/yourusername/project",
  "date": "YYYY-MM-DD"
}
```

Place project images in the `static/images` directory.

### Articles

Update the `data/articles.json` file to add your own articles. Each article should follow this format:

```json
{
  "id": "unique-article-id",
  "title": "Article Title",
  "content": "Full article content in HTML format...",
  "image": "article-image.jpg",
  "tags": ["Machine Learning", "Tutorial"],
  "date": "YYYY-MM-DD"
}
```

Place article images in the `static/images` directory.

## Adding Visualizations and Graphics

For future visualization needs, you can integrate:

- Plotly for interactive charts
- D3.js for custom visualizations
- Bokeh for Python-based interactive visualizations

To add these libraries:

1. Install the required Python packages:

```bash
pip install plotly dash bokeh
pip freeze > requirements.txt
```

2. Create a new route in `app.py` for your visualization:

```python
@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')
```

3. Create a new template for your visualizations in `templates/`.

## Deployment Options

### PythonAnywhere

1. Sign up for a [PythonAnywhere](https://www.pythonanywhere.com/) account.
2. Upload your code or clone your GitHub repository.
3. Create a new web app using Flask.
4. Configure the web app to point to your `app.py` file.

### Heroku

1. Create a `Procfile` in the root directory:
   ```
   web: gunicorn app:app
   ```

2. Add gunicorn to requirements.txt:
   ```
   gunicorn==20.1.0
   ```

3. Deploy to Heroku following their Python application deployment guide.

## License

This project is open source and available under the [MIT License](LICENSE).
