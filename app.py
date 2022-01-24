from wtforms.validators import ValidationError
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from text_file import TextFile ,allowed_file_type
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods=['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)

        filename = secure_filename(f.filename)

        if '.' not in filename:
            raise ValidationError({"file":"File has no file extension"})
        file_type = filename.split(".")[-1]

        if file_type.lower() not in allowed_file_type():
            raise ValidationError({"file":"unsupported file type"})
            return render_template()
            

        
        # store uploaded files in static folder
        f.save(app.config['UPLOAD_FOLDER'] + filename)
        new_file = TextFile(filename)
        sorted_values = new_file.read_and_sort_file()
        new_file.write_sorted_names(sorted_values)

    return render_template('content.html', content=sorted_values)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
