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
    {'title': 'IBM Cloud Private',
     'short_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.',
     'long_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.LONG VERSION',
     'project_link': 'https://www.ibm.com/cloud/private',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },

    {'title': 'Travis on Z',
     'project_link': 'github.com/bendermIBM/travis-cookbooks',
     'short_description': 'Enabling the tool that enables the tools - on Linux on Z.',
     'long_description': 'Enabling the tool that enables the tools - on Linux on Z.LONG VERSION',
     'featured': True,
     'tags': 'Travis'
     },
    {'title': 'NexNest',
     'project_link': 'github.com/maxbbender/nexnest',
     'short_description': 'Student housing portal built with love by @Max Bender and @Mike Mcginnis',
     'long_description': 'I had written a couple websites with Flask in school, but wanted to learn more and read up on Miguel Grinberg’s Flask tutorial and was exposed to a new set of best practices. Approached with an idea for a rental website targeted at students we designed and implemented a website written in Python. Backed by a fairly complex database that featured notifications and recursive comments, SQLAlchemy handles most of the direct SQL queries the complex JOINs.',
     'featured': True,
     'tags': 'Kubernetes,Python'
     },
    {'title': 'Viral Education/TALOS',
     'project_link': 'github.com/maxbbender/Viral-Education',
     'short_description': 'TALOS (Textual Augmentation Learning of Semantics), a Web-based platform for vocabulary acquisition that provides capabilities for analytics to support learning of vocabulary. This software prototype, currently in beta-testing, supports differentiated learning as well as common coursework, allowing users to contribute and access text while promoting ease of reading.',
     'long_description': 'The first real website I made for someone other than myself. Written in PHP in a summer alongside working at the Marist College HelpDesk, this website was part of a research project that funded me to present at INTED in Madrid, Spain. Alongside two professors, I gave a presentation on using technology to enhance learning in an un-obtrusive fashion with a concentration in learning foreign languages.'

     'Backed by a MySQL database this is where I learned a lot about security in the modern age of web-development. Certain vulnerabilities such as SQL Injections and XSS were ones that I focused on researching because I knew they were some of the more common avenues of attack. Looking back on it however I have already noticed some mistakes but I was happy with how it came out.',
     'featured': True,
     'tags': 'PHP'
     },
    {'title': 'Let\'s Talk',
     'project_link': '',
     'short_description': 'Short hands-on education modules surrounding a specific technology or a group of technologies together.',
     'long_description': 'Teaching others and seeing that lightbulb go off is and experience that I get a lot of gratification from. In my effort to educate teams at IBM I realized that giving the same presentation to team after team was an inefficient method. So I created “Let’s Talk” which is a group of education modules that have an intense focus on hands-on learning using examples hosted on GitHub. We scheduled live presentations and recorded them for future consumption and they featured code examples accompanied by a tutorial-like presentation.'

     'It began with connecting the travis-ci worker to an Openstack instance hosted on z/KVM. However we ran into issues with big bursts of builds which caused the networking layer in Openstack to intermittently not initiate. Eventually we upgraded to use LXD to run the builds which gave a huge speed increase and more portability. Using Packer I built xenial/bionic base images for Linux on Z and deployed a production configuration supporting 20,000+ builds a year.'

     'See some changes to the travis-build scripts which also needed some configuartions.'

     'Once I moved to the LXD based builds I was able to automate the deployment of LXD and the Travis Worker on a Ubuntu Bionic host using Ansible. Still using the previous OpenStack environment we could now provision infrastructure with Terraform and configure workers using Ansible.',
     'featured': False,
     'tags': ''
     }
]

collabs = [
    {'fname': 'Max', 'lname': 'Bender', 'name': 'MaxBender', 'clink': 'linkMB'},
    {'fname': 'Zac', 'lname': 'Bender', 'name': 'ZacBender', 'clink': 'linkZB'},
    {'fname': 'Kasey', 'lname': 'Leahy', 'name': 'KaseyLeahy', 'clink': 'linkKL'},
    {'fname': 'Tom', 'lname': 'Rowles', 'name': 'TomRowles', 'clink': 'linkTR'},
]

aboutmes = [
    {'title': 'Principal Engineer',
     'subtitle': "I'm Max Bender a Principal Engineer specializing in CICD and DevOps solutions.",
     'description': 'Primarily, my work has been on CICD and DevOps solutions, but I often get this itch to create something new. Python is my go-to scripting language but I’m not afraid of a little Bash or Ruby if the use-case calls for it or I am trying to work with a library that requires the aforementioned (i.e Chef). The instant gratification of making websites and working with complex relational database setups is a puzzle that I relish. Using Flask and SQLAlchemy I have put together some complex websites as a consultant on the side. See the NexNest project as an example.',
     'quote': '[being a Principal Engineer] is far more strategic, it’s far more business oriented, it’s involving a lot more influence, being an influencer without having the management title. [during the time becoming a Principal Engineer you] need to be a force multiplier. There was a clear transition from me writing code to teaching others how to write code that’s actually clean and doesn’t cause us trouble too fast down the line. One of the big parts of Principal Engineering in my mind is you teach more than you actually do yourself.'}
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
    {'username': 'admin', 'password': 'asdf1234'}
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
