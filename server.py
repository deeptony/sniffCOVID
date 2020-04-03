#performing relevant imports
from flask import Flask, render_template, request, abort, session, flash, redirect

#instantiating server
server = Flask("flask_server")

#defining profiles
profiles = {
'Antonio':{'education':'IE University', 'educationContent': 'Coding is all he does from Monday to Friday',\
    'career':'Club promoter',  'careerContent': 'He loves to party',\
    'main hobby':'Surfing',  'main_hobby_Content': 'He believes catching waves is all you need',\
    'img':'/static/img/antonio.png'},
'Ale':{'education':'ITBA', 'educationContent': "Studied electrical engineering at Buenos Aires' institute of technology",\
    'career':'Engineer',  'careerContent': 'Has worked at some startups',\
    'main hobby':'Running',  'main_hobby_Content': 'More into quick, short distance runs!',\
    'img':'/static/img/ale.jpg'},
'Janik':{'education':'IE University', 'educationContent': 'Previously studied business at EBS University in Germany (near Frankfurt)',\
    'career':'Business Consultant, Start-Ups',  'careerContent': 'Experience at Consulting with Porsche AG in Stuttgart.',\
    'main hobby':'Gaming and Quarantine',  'main_hobby_Content': 'World of Warcraf: Classic',\
    'img':'/static/img/janik.jpg'},
'Felipe':{'education':'UPB Boliviana', 'educationContent': "Studied Business Administration at Private University of Bolivia",\
    'career':'Business Administration, Entrepreneur',  'careerContent': '7 years of experience as General Manager of small businesses, 2 years of experience as Business Owner & Co-founder',\
    'main hobby':'Parenting, Cooking, Travelling, Swimming, Audio',  'main_hobby_Content': 'Love to cook for my family and listen to music with a good cup of coffee',\
    'img':'/static/img/felipe.jpg'},
}

#defining courses
courses = {
'AI':{'length':'15 sessions','length-content':'placeholder',\
    'difficulty':'High', 'difficulty-content':'placeholder',\
    'rating':'9/10', 'rating-content':'placeholder',\
    'img':'/static/img/atom.png'},
'TIP':{'length':'100 sessions','length-content':'Great!',\
    'difficulty':'High', 'difficulty-content':'Pretty difficult but in the end we all managed to do it.',\
    'rating':'8/10', 'rating-content':'Would not recommend!',\
    'img':'/static/img/atom.png'},
'BIT':{'length':'1 session','length-content':'Very disappointing course with little to none take away.',\
    'difficulty':'Easy', 'difficulty-content':'Easy because we did not have any classes.',\
    'rating':'7/10', 'rating-content':'Maybe less.',\
    'img':'/static/img/atom.png'},
'DataEngineering':{'length':'15 sessions','length-content':'placeholder',\
    'difficulty':'Master Level', 'difficulty-content':'placeholder',\
    'rating':'9/10', 'rating-content':'placeholder',\
    'img':'/static/img/atom.png'},
'Python':{'length':'15 sessions','length-content':'placeholder',\
    'difficulty':'Master Level', 'difficulty-content':'placeholder',\
    'rating':'11/10', 'rating-content':'placeholder',\
    'img':'/static/img/atom.png'},
'JS':{'length':'15 sessions','length-content':'placeholder',\
    'difficulty':'Master Level', 'difficulty-content':'placeholder',\
    'rating':'12/10', 'rating-content':'placeholder',\
    'img':'/static/img/atom.png'},
'Cloud':{'length':'15 sessions','length-content':'placeholder',\
    'difficulty':'Medium Level', 'difficulty-content':'placeholder',\
    'rating':'8.5/10', 'rating-content':'placeholder',\
    'img':'/static/img/atom.png'},
}
#defining routes

#route for landing page
@server.route('/')
def render_index():
    return render_template('landing.html')


#route to get dict with profiles
@server.route('/profiles/')
def render_profiles():
    #rendering dict with person´s information
    info_dict = profiles
    return info_dict

#route to render profile.html with name of profile
@server.route('/profiles/<n>')
def render_profile(n):
    name = n
    return render_template('profile.html', name = name)

#route to get dict with courses
@server.route('/courses/')
def render_courses():
    #rendering dict with person´s information
    info_dict = courses
    return info_dict

#route to render course.html with name of course
@server.route('/courses/<n>')
def render_course(n):
    #rendering dict with person´s information
    name = n
    return render_template('course.html', name = name)

#statement to initiate server
if __name__ == '__main__':
    server.run(debug = True)
