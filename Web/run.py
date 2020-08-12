from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from model.inference import model_inference
import os
import sys

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('/home/index.html')

@app.route('/index')
def index():
    return render_template('/home/index.html')

@app.route('/<template>')
def route_template(template):
    if not template.endswith('.html'):
        template+='.html'
    if "performance" in template:
        return render_template('/home/'+template)
    etc = ['basic','buttons','chartjs','dropdowns','typography']
    for tmp in etc:
        if tmp in template:
            return render_template(template)

    return render_template('/cancer_result/'+template)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      print("run", os.getcwd(), file=sys.stderr)
      print("run", os.getcwd(), file=sys.stdout)
      #저장할 경로 + 파일명
      f.save('/app/Web/input/'+secure_filename(f.filename))
      cohort, name, top_labels, top_normal, top_input = model_inference(f.filename)
      return render_template('/home/predict.html', cohort=cohort, name=name,
                            labels=top_labels, normal=top_normal, input=top_input)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as ex:
        print(ex)
