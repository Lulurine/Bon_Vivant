# Bon Vivant Perfume Website

## Overview
Bon Vivant is a web application designed to showcase a variety of perfumes. The application allows users to browse products, view detailed information about each perfume, learn about the brand's story, and manage their account.

## Project Structure
```
Bon Vivant
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── index.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── brand_story.html
│   │   └── account.html
│   └── static
│       └── style.css
├── perfume.db
├── requirements.txt
├── config.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd Bon Vivant
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Set up the database by running the necessary migrations (if applicable).
2. Start the Flask application:
   ```
   flask run
   ```
3. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Features
- Home page displaying the main content.
- Product list showcasing all available perfumes.
- Detailed view for each perfume.
- Brand story page providing background information.
- User account management.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.