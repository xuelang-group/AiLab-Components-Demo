import suanpan
from suanpan.app import app
from suanpan.app.arguments import String


@app.input(String(key="inputData1", alias="name", default="Suanpan"))
@app.output(String(key="outputData1", alias="result"))
def hello_world(context):
    args = context.args
    return f"Hello World, {args.name}!"


if __name__ == "__main__":
    suanpan.run(app)
