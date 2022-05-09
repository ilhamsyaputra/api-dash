from app import app

# routes
from src.routes import display_page

# page layout
from src.components.layout import layout

# api
from src.api.routes import api

# load layout
app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)