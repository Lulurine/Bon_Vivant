# Bon Vivant Perfume Website

## Overview
Bon Vivant is a web application designed to showcase a variety of perfumes. The application allows users to browse products, view detailed information about each perfume, learn about the brand's story, and manage their account.

## Project Structure
```
Bon_Vivant/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── brand_story.html
│   │   └── account.html
│   └── static/
│       └── style.css
├── perfume.db
├── requirements.txt
├── config.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone git@github.com:Lulurine/Bon_Vivant.git
   ```
2. Navigate to the project directory:
   ```
   cd Bon_Vivant
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask application:
   ```
   flask run
   ```
2. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Features
- Home page introduces the application and brand story.
- Browse a comprehensive list of perfumes.
- Categorize perfumes by gender for easier browsing.
- Perfumes are ranked based on view counts.
- View detailed information for each perfume.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.