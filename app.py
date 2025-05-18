from flask import Flask, render_template, request, send_file
from markupsafe import Markup
from xhtml2pdf import pisa
import io

app = Flask(__name__)

# Route for the resume input form
@app.route('/')
def index():
    return render_template('form.html')

# Route to display the resume preview
@app.route('/resume', methods=['POST'])
def resume():
    data = request.form.to_dict()
    return render_template('resume.html', data=data)

# Route to generate and download the resume PDF
@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.form.to_dict()
    html = render_template('resume.html', data=data)

    # Convert HTML to PDF
    result = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html), dest=result)

    if not pisa_status.err:
        result.seek(0)
        return send_file(result, download_name='resume.pdf', as_attachment=True)
    else:
        return "PDF generation failed."
    
@app.template_filter('nl2br')
def nl2br_filter(s):
    if not s:
        return ''
    return Markup(s.replace('\n', '<br>'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)