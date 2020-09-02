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
     'long_description': 'Enabling the tool that enables the tools - on Linux on Z.LONG VERSION'},
    {'title': 'IBM Cloud Private',
     'short_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.',
     'long_description': 'IBM Cloud™ Private is a reliable and scalable cloud platform that runs on your infrastructure. It’s built on open source frameworks, like containers, Kubernetes and Cloud Foundry.LONG VERSION',
     'project_link': 'https://www.ibm.com/cloud/private'
     }
]


def seed_tags(db):

    # Generate a List of Tags to be seeded
    tag_list = []

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
                              project['project_link'],
                              project['short_description'],
                              project['long_description']
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
