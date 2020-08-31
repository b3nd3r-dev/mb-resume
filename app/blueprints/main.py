from random import shuffle

from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Project, Tag

main = Blueprint('main', __name__, template_folder='../templates')


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@main.route('/')
def index():

    # Query all Tags and Shuffle the output
    all_tags = Tag.query.all()
    shuffle(all_tags)

    # Split tags into 3 different lists https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    split_tag_list = list(chunks(all_tags, int(len(all_tags) / 3)))

    print(split_tag_list)
    print(type(split_tag_list))
    first_tag_list = split_tag_list[0]
    second_tag_list = split_tag_list[1]
    third_tag_list = split_tag_list[2]

    if len(split_tag_list) > 3:
        third_tag_list.extend(split_tag_list[3])

    return render_template('index.html',
                           first_tag_list=first_tag_list,
                           second_tag_list=second_tag_list,
                           third_tag_list=third_tag_list
                           )


@ main.route('/contact')
def contact():
    return render_template('contact.html')


@ main.route('/project')
def project():
    return render_template('project.html',
                           #    p_name=Project.title
                           #    p_link=Project.project_link
                           #    p_tags=Tag.project.tags
                           #    p_short_desc=Project.short_description
                           )


@ main.route('/projectdetail')
def projectdetail():
    return render_template('projectdetail.html')

# @main.route('/test')
# @main.route('/test/<poopy>')
# def test(poopy='biatch'):
#     somelist = [1,2,3,4,5]
#     print (poopy)
#     return render_template('test.html', somelist=somelist, peepee=poopy)
