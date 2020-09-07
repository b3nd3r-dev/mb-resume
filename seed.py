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
    {'title': 'Travis on Z',
     'project_link': 'github.com/bendermIBM/travis-cookbooks',
     'short_description': 'Enabling the tool that enables the tools - on Linux on Z.',
     'long_description': 'Enabling the tool that enables the tools - on Linux on Z.LONG VERSION', 'featured': True},

    {'title': 'IBM Cloud Private',
     'short_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.',
     'long_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.LONG VERSION',
     'project_link': 'https://www.ibm.com/cloud/private',
     'featured': True
     },

    {'title': 'NexNest',
     'project_link': 'github.com/maxbbender/nexnest',
     'short_description': 'Student housing portal built with love by @Max Bender and @Mike Mcginnis',
     'long_description': 'I had written a couple websites with Flask in school, but wanted to learn more and read up on Miguel Grinberg’s Flask tutorial and was exposed to a new set of best practices. Approached with an idea for a rental website targeted at students we designed and implemented a website written in Python. Backed by a fairly complex database that featured notifications and recursive comments, SQLAlchemy handles most of the direct SQL queries the complex JOINs.',
     'featured': True
     },

    {'title': 'Let\'s Talk',
     'project_link': '',
     'short_description': 'Short hands-on education modules surrounding a specific technology or a group of technologies together.',
     'long_description': 'Teaching others and seeing that lightbulb go off is and experience that I get a lot of gratification from. In my effort to educate teams at IBM I realized that giving the same presentation to team after team was an inefficient method. So I created “Let’s Talk” which is a group of education modules that have an intense focus on hands-on learning using examples hosted on GitHub. We scheduled live presentations and recorded them for future consumption and they featured code examples accompanied by a tutorial-like presentation.'

     'It began with connecting the travis-ci worker to an Openstack instance hosted on z/KVM. However we ran into issues with big bursts of builds which caused the networking layer in Openstack to intermittently not initiate. Eventually we upgraded to use LXD to run the builds which gave a huge speed increase and more portability. Using Packer I built xenial/bionic base images for Linux on Z and deployed a production configuration supporting 20,000+ builds a year.'

     'See some changes to the travis-build scripts which also needed some configuartions.'

     'Once I moved to the LXD based builds I was able to automate the deployment of LXD and the Travis Worker on a Ubuntu Bionic host using Ansible. Still using the previous OpenStack environment we could now provision infrastructure with Terraform and configure workers using Ansible.',
     'featured': False
     },

    {'title': 'Viral Education/TALOS',
     'project_link': 'github.com/maxbbender/Viral-Education',
     'short_description': 'TALOS (Textual Augmentation Learning of Semantics), a Web-based platform for vocabulary acquisition that provides capabilities for analytics to support learning of vocabulary. This software prototype, currently in beta-testing, supports differentiated learning as well as common coursework, allowing users to contribute and access text while promoting ease of reading.',
     'long_description': 'The first real website I made for someone other than myself. Written in PHP in a summer alongside working at the Marist College HelpDesk, this website was part of a research project that funded me to present at INTED in Madrid, Spain. Alongside two professors, I gave a presentation on using technology to enhance learning in an un-obtrusive fashion with a concentration in learning foreign languages.'

     'Backed by a MySQL database this is where I learned a lot about security in the modern age of web-development. Certain vulnerabilities such as SQL Injections and XSS were ones that I focused on researching because I knew they were some of the more common avenues of attack. Looking back on it however I have already noticed some mistakes but I was happy with how it came out.',
     'featured': True
     }
]


def seed_tags(db):

    # Generate a List of Tags to be seeded
    tag_list = []

    # A tag has attributes
    for tag in tags:
        new_tag = Tag(tag['name'], tag['knowledge'])
        tag_list.append(new_tag)

    print(tag_list)

    # Add Tags to Database
    for tag in tag_list:

        # First check if Tag exists
        tag_query = Tag.query.filter_by(name=tag.name).first()

        if not tag_query:
            db.session.add(tag)

    db.session.commit()


def seed_projects(db):

    # Generate a list of tags to be seeded
    project_list = []

    for project in projects:
        new_project = Project(project['title'],
                              project['short_description'],
                              project['long_description'],
                              project['featured'],
                              project['project_link']
                              )
        project_list.append(new_project)

        print(project_list)

        # Add Project to Database
        for project in project_list:

            # First check if Project exists
            project = Project.query.filter_by(title=project.title).first()

            if not project:
                db.session.add(new_project)

        db.session.commit()
