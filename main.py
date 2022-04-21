import helper.fileManage as fileManage


from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/lawrence")
def lawrence():
    return "Hello, Lawrence!"


@app.route("/")
def home():
    return render_template("home.html", ModVersions = fileManage.getModVersions())

@app.route("/about")
def about():
    return render_template("about.html", ModVersions = fileManage.getModVersions())

@app.route("/about_lawrence")
def about_lawrence():
    return render_template("about_lawrence.html", ModVersions = fileManage.getModVersions())

@app.route("/versions")
def versions():
    return render_template("versions.html", Mods = fileManage.getMods(request.args.get("version")),
                           ModVersions = fileManage.getModVersions(), Version=request.args.get("version"), ModsPlaceHolder = fileManage.GetArray(fileManage.getMods(request.args.get("version")), fileManage.GetMineCraftMods()))

@app.route("/activate", methods = ['POST'])
def activate():
    fileManage.MoveMod(request.args.get("version"))
    return render_template("versions.html", Mods=fileManage.getMods(request.args.get("version")),
                           ModVersions=fileManage.getModVersions(), Version=request.args.get("version"),ModsPlaceHolder = fileManage.GetArray(fileManage.getMods(request.args.get("version")), fileManage.GetMineCraftMods()))


if __name__ == "__main__":
    app.run(debug=True)


