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
