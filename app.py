from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    cover_letter = request.form.get('coverLetter')
    job_description = request.form.get('jobDescription')
    
    prompt = f"""You are a college student who graduated from Loyola Chicago with a bachelor's degree in computer science with a minor in philosophy. You graduate with a 3.0 and are currently hunting for a job. You graduate with may 2023 and it is now august 2023 and are willing to start ASAP. Now, you are tasked with making a cover letter for a job. You have a cover letter already written but it is not for the job you wish to apply for. Write a new cover letter for the job description given. Make the cover letter as similar as possible to the cover letter given, but also make it fit the job description. Cover Letter: {cover_letter} , Job description: {job_description}"""

    return jsonify({'prompt': prompt})

if __name__ == '__main__':
    app.run(debug=True)
