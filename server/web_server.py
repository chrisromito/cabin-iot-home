from sanic import Sanic
from sanic.response import html
from settings import Settings
from blueprints.register import blueprints


app = Sanic('server')
app.update_config(Settings)
app.static(Settings.STATIC_URL, Settings.STATIC_PATH)
print(Settings.DB_PATH)

for blueprint in blueprints:
    app.blueprint(blueprint)


@app.get('/')
async def home(request):
    print('home view()')
    return html(get_base_template())


def get_base_template():
    with open(Settings.TEMPLATE_PATH, 'r') as template:
        return template.read()
