from flask import Flask, render_template
app = Flask(__name__, template_folder='./templates', static_folder='./assets')

obj={}

@app.route('/')
def home():
    obj["title"]="Personal Webpage | David W Sosa "
    obj["style"]="assets/css/style.css"
    obj["logic"]="assets/js/logic.js"
    return render_template('child.html', obj=obj)

if __name__ == "__main__":
    app.run(debug=True)