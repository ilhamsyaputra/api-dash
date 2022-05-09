from app import app
from dash.dependencies import Input, Output

from src.pages.index import index
from src.pages.page1 import page1
from src.pages.page2 import page2

@app.callback(
    Output(component_id='page-content', component_property='children'),
    Input(component_id='url', component_property='pathname')
)
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout