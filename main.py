#Import Flask components
from flask import Flask, render_template, request, redirect, jsonify


#Import Secure filename for files
from werkzeug.utils import secure_filename


#import os to access file system
import os


#Set Image Upload Folder
UPLOAD_FOLDER = 'images'


#Set Allowed Extensions
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


#Initialize flask app
app = Flask(__name__)


#Set some secret key
app.secret_key = "secret key"


#Set configration for files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


#Function to check if file extension is allowed
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#Route to render homepage of an app
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


#Route to receive image
@app.route('/image', methods=['POST'])
def upload_file():

	# check if the post request has the file part
	if 'image' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp

	file = request.files['image']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp

	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp

	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


#Run flask app
app.run()
