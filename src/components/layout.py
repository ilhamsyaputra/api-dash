import dash_html_components as html
import dash_core_components as dcc

from src.components.navbar import navbar

layout = html.Div([
    dcc.Location(id='url', refresh=False),

    # navbar header
    navbar,

    # content
    html.Div(
        id='page-content',
        style={
            'margin-left': '15rem',
        }
    )
])