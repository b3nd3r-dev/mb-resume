from app.models import *

tags = [
    {'name': 'Travis', 'knowledge': 'fluent'},
    {'name': 'Python', 'knowledge': 'fluent'},
    {'name': 'Kubernetes', 'knowledge': 'fluent'},
    {'name': 'Flask', 'knowledge': 'fluent'},
    {'name': 'Docker', 'knowledge': 'fluent'},
    {'name': 'Ansible', 'knowledge': 'fluent'},
    {'name': 'Linux', 'knowledge': 'fluent'},
    {'name': 'Git', 'knowledge': 'fluent'},
    {'name': 'KVM', 'knowledge': 'fluent'},
    {'name': 'Elastic', 'knowledge': 'proficient'},
    {'name': 'Grafana/Prometheus', 'knowledge': 'proficient'},
    {'name': 'Elastic', 'knowledge': 'proficient'},
    {'name': 'SQLAlchemy', 'knowledge': 'proficient'},
    {'name': 'PHP', 'knowledge': 'proficient'},
    {'name': 'Terraform', 'knowledge': 'proficient'},
    {'name': 'Jenkins', 'knowledge': 'proficient'},
    {'name': 'Ruby', 'knowledge': 'familiar'},
    {'name': 'Packer', 'knowledge': 'familiar'},
    {'name': 'AWS', 'knowledge': 'familiar'},
    {'name': 'Chef', 'knowledge': 'familiar'},
    {'name': 'RabbitMQ', 'knowledge': 'familiar'},
    {'name': 'Postgres', 'knowledge': 'familiar'},
    {'name': 'Redis', 'knowledge': 'familiar'},
    {'name': 'OpenStack', 'knowledge': 'familiar'},
]

projects = [
    {'title': 'Delete Me',
     'short_description': 'Delete Me',
     'long_description': 'Delete Me',
     'project_link': 'Delete Me',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },
    {'title': 'Delete Me2',
     'short_description': 'Delete Me',
     'long_description': 'Delete Me',
     'project_link': 'Delete Me',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     }
]

collabs = [
]

aboutmes = [
    {'title': 'Principal Engineer',
     'subtitle': "I'm Max Bender a Principal Engineer specializing in CICD and DevOps solutions.",
     'description': '',
     'quote': ''}
]

achievements = [
    {'name': 'Moses Brown',
     'start_date': '2011',
     'end_date': '2014',
     'desc': 'Moses Brown School is a Quaker school located in Providence, Rhode Island offering pre-kindergarten through secondary school classes.',
     'link': '',
     'link_name': '',
     'icon': 'fas fa-school'
     },

    {'name': 'Marist College',
     'start_date': '2014',
     'end_date': '2017',
     'desc': 'Participated in the MCCS and many other community activities which strengthend my value as a teamate and leader. Graduated w/ my Major’s GPA at 3.8 with Honors and Deans List.',
     'link': '',
     'link_name': '',
     'icon': 'fas fa-school'
     },

    {'name': 'Help Desk Operator',
     'start_date': '2014',
     'end_date': '2015',
     'desc': 'While my time at the Help Desk wasn’t the most glamorous, I valued it a lot. I was resetting passwords and helping people out with basic technology issues but during that I was gaining so much experience in talking with customers. We were on the phone or helping people in person and looking back on it this experience has strengthened my ability to interact with customers in the field at IBM',
     'link': 'https://www.marist.edu/',
     'link_name': 'Marist',
     'icon': 'fas fa-info'
     },

    {'name': 'Principal Test Engineer',
     'start_date': '2015',
     'end_date': 'Present',
     'desc': 'At IBM I started on the zPET solution test organization which tests the mainframe in a full stack customer-like configuration. Shortly after I moved to a team called the Linux Center of Competence which focused on testing Linux on Z with a similar configuration as on zPET. Part of the teams mission was to remove excuses when it came to running software on Linux on Z.',
     'link': 'https://www.ibm.com/us-en/',
     'link_name': 'IBM',
     'icon': 'fas fa-server'
     },
]

users = [
    {'username': 'bender', 'password': 'HXGsJuDBppq1gixF4LGn'}
]


def seed_tags(db):
    for tag in tags:
        tag_to_check = Tag.query.filter_by(name=tag['name']).first()
        if not tag_to_check:
            new_tag = Tag(tag['name'],
                          tag['knowledge'])
            db.session.add(new_tag)
            db.session.commit()
            # print(tag['name'] + ' commited')
        else:
            pass
            # print('Tag already exists')


def seed_projects(db):
    for project in projects:
        project_to_check = Project.query.filter_by(title=project['title']).first()
        if not project_to_check:
            new_project = Project(
                project['title'],
                project['short_description'],
                project['long_description'],
                project['featured'],
                project['project_link']
            )

            db.session.add(new_project)
            db.session.commit()
            # print(project['title'] + ' commited')

            tags_list = project['tags'].split(',')
            for a_tag in tags_list:
                tag_to_add = Tag.query.filter_by(name=a_tag).first()
                if tag_to_add:
                    new_project.tags.append(tag_to_add)
                    db.session.commit()
        else:
            pass
            # print('Project already exists')


def seed_collabs(db):
    for collab in collabs:
        collab_to_check = Collab.query.filter_by(fname=collab['fname'],
                                                 lname=collab['lname']).first()
        if not collab_to_check:
            new_collab = Collab(collab['fname'],
                                collab['lname'],
                                collab['name'],
                                collab['clink']
                                )
            db.session.add(new_collab)
            db.session.commit()
        else:
            pass
            # print('Collab already exists')


def seed_aboutme(db):
    for aboutme in aboutmes:
        aboutme_check = AboutMe.query.filter_by(title=aboutme['title']).first()
        if not aboutme_check:
            new_aboutme = AboutMe(
                aboutme['title'],
                aboutme['subtitle'],
                aboutme['description'],
                aboutme['quote']
            )
            db.session.add(new_aboutme)
            db.session.commit()
        else:
            pass
            # print('Homepage item already exists')


def seed_achievements(db):
    for achievement in achievements:
        achievement_check = Achievement.query.filter_by(name=achievement['name'],
                                                        start_date=achievement['start_date']).first()
        if not achievement_check:
            new_ach = Achievement(
                achievement['name'],
                achievement['start_date'],
                achievement['end_date'],
                achievement['desc'],
                achievement['link'],
                achievement['link_name'],
                achievement['icon']
            )
            db.session.add(new_ach)
            db.session.commit()

        else:
            pass
            # print('Achievement already exists')


def seed_users(db):
    for user in users:
        user_to_check = User.query.filter_by(username=user['username']).first()

        if not user_to_check:
            new_user = User(user['username'],
                            user['password'])
            db.session.add(new_user)
            db.session.commit()
