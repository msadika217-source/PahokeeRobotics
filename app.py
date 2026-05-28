import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('PahokeeRoboticsIndex.html')

@app.route('/PahokeeRoboticsIndex.html')
def index():
    return render_template('PahokeeRoboticsIndex.html')

@app.route('/AboutUs.html')
def about():
    return render_template('AboutUs.html')

@app.route('/ContactUs.html')
def contact():
    return render_template('ContactUs.html')

@app.route('/Awards.html')
def awards():
    return render_template('Awards.html')   

@app.route('/Calendar.html')
def calendar():
    return render_template('Calendar.html')

# --- AUTOMATED GALLERY ROUTE ---
@app.route('/Gallery.html')
def gallery():
    # The exact folder where your 100+ pictures sit
    folder_path = 'static/images/Gallery'
    gallery_images = []
    
    if os.path.exists(folder_path):
        for filename in os.listdir(folder_path):
            # Grab images (including PNG, JPG, JPEG, GIF)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Creates the clean web path: /static/images/Gallery/filename.png
                web_path = f"/{folder_path}/{filename}"
                gallery_images.append(web_path)
                
    # Send the list directly to your HTML template as 'Gallery'
    return render_template('Gallery.html', Gallery=gallery_images)

@app.route('/Outreach.html')
def outreach():
    return render_template('Outreach.html')

@app.route('/Resources.html')
def resources():
    return render_template('Resources.html')

@app.route('/Sponsors.html')
def sponsors():
    return render_template('Sponsors.html') 

@app.route('/Teams.html')
def teams():
    return render_template('Teams.html')

@app.route('/MiddleSchool.html')
def middle_school():
    return render_template('MiddleSchool.html')


@app.route('/HighSchool.html')
def high_school():
    return render_template('HighSchool.html')

@app.route('/BenderBots.html')
def bender_bots():
    return render_template('BenderBots.html')

@app.route('/OverviewBB.html')
def overview_bb():
    return render_template('OverviewBB.html')

@app.route('/Rising_Phoneix.html')
def rising_phoenix():
    return render_template('Rising_Phoneix.html')   

@app.route('/OverviewRP.html')
def overview_rp():
    return render_template('OverviewRP.html')

@app.route('/Dynamics.html')
def dynamics():
    return render_template('Dynamics.html')

@app.route('/Mechatrons.html')
def mechatrons():
    return render_template('Mechatrons.html')

@app.route('/OverviewM.html')
def overview_m():
    return render_template('OverviewM.html')

if __name__ == '__main__':
    app.run(debug=True)