from flask import Flask, render_template, request
from practice_regex import searchbyreg

application=Flask(__name__)

@application.route('/')
def index():
    pattern=request.args.get("pattern", "")
    if pattern:
        result=matchwith(pattern)
    else:
        result=""
    return render_template("entry.html", the_results=result)

@application.route("/entry")
def matchwith(pattern):
    try:
        result=str(searchbyreg(pattern))
        return result
    except ValueError:
        return "недействительный ввод"

application.run(debug=True)
