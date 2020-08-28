from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__, template_folder='../templates')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/project')
def project():
    return render_template('project.html')
    
@main.route('/projectdetail')
def projectdetail():
    return render_template('projectdetail.html')

# @main.route('/test')
# @main.route('/test/<poopy>')
# def test(poopy='biatch'):
#     somelist = [1,2,3,4,5]
#     print (poopy)
#     return render_template('test.html', somelist=somelist, peepee=poopy)
    