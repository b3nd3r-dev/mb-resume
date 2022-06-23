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
    {'name': 'Project-Management', 'knowledge': 'familiar'},
]

projects = [
    {'title': 'KVM Solution Test',
     'short_description': 'A customer-e KVM Hypervisor',
     'long_description': 'Back in July of 2020, I took over the role as a Technical Team Lead for the KVM Solution Test project. When I joined, there were was a foundation of automation but I quickly identified areas that could be improved on. Over the next 6 months my team and I worked to achieve a goal of 100% automated coverage of the test cases we were responsible for. We have achieved that goal and now are functioning as a mature development orginization, evaluating new line items/features as they arise and have begun the process to modularlize & externalize our environment.<br>We worked with the 3 major linux distributions (RHEL/SLES/Ubuntu) during their Beta testing periods to verify KVM on their platforms. It was a challenging endeavor maintaining our relationships with 3 different sets of engineers, but I ended up learning a lot from the process about manging priorities and expectations for my team. Where applicable we accomidated large scale testing scenarios (involving 10TB+ of RAM or 1000+ KVM guests) which provided a unique value-add to the community, verifying the platform at an enterprise scale.<br>The DevOps framework was built with <mark>Ansible</mark> and consisted of 25k+ lines of code. We approached the framework with an Agile methodology in mind by building an MVP, getting hands on the solution in order to identify the next required evolution. It is going great with over 200 pull requests merged to date, and many more new ones currently open. The power of our collaboration across the team has built in an incredible level of resiliency to the code base, setting the team up to continue to innovate for years to come.',
     'featured': True,
     'tags': 'KVM,Project-Management,Ansible'
     },
    {'title': 'Travis on Z',
     'short_description': 'Enabling the ',
     'long_description': 'A big part of my voyage in OpenSource has been learning how to use CICD tools to build automation around a product. For me it was a necessity, because the tediousness of re-running builds had gotten to vast. Travis offers a free CICD mechanism hooked natively into GitHub and many of the projects I was looking at were using it in their pipelines.\nInternally we had a <mark>Travis</mark> environment for `x86` and `ppc64le`, but none for `s390x`. I was tasked with supporting Travis on Linux on Z and so began a month dive into the source code of Travis. With this we were able to enable a regression pipeline for the release for IBM Cloud Private (ICP) on Z, a <mark>Kubernetes</mark> offering by IBM.\nIn collaboration with my team lead and STSM @ IBM, Jay Brenneman, we built and ported the Travis codebase to `s390x`. Jay focused on the hypervisor end, initially hooking <mark>OpenStack</mark> up to z/VM and eventually moving to <mark>KVM</mark> on Linux on Z. Meanwhile I focused on the provisioning tools that largely make up the magic of Travis. Largely this consisted of <mark>Chef</mark> cookbooks and custom bash scripts and took some 3 weeks to get our first working build, but it was glorious.\nFor the first time ever our developers were able to modify their Travis pipelines and run their builds on Linux on Z. However as they integrated the `s390x` builds, all of a sudden Travis on Z became mission critical to all of ICP development due to the nature of Travis and GitHub. If even one architecture fails to pass, Travis will block code from being merged into the `master` branch. When Travis on Z took an outage, the messages and alerts quickly started flooding in. After our second extended outage we quickly realized that we had to come up with a highly available solution for the tool.\nUtilizing a load balancing feature in <mark>RabbitMQ</mark> we stood up another OpenStack instance located in Hursley, United Kingdom and replicated our port of Travis on Z to those systems. Since then we have been able to take independent outages without affecting an ever growing demand for Travis on Z.',
     'project_link': 'https://github.com/bendermIBM/travis-cookbooks',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },
     {'title': 'IBM Cloud Private',
     'short_description': 'IBM Cloud™ Private .',
     'long_description': '    My team was tasked with supporting a release of IBM Cloud Private (ICP), a <mark>Kubernetes</mark> offering by IBM, on Linux on Z. Our goal was to have full support by the 3.1.2 release and to do this we ported Travis to the Mainframe as mentioned above.\nAlongside these efforts we saw an opportunity to further drive our teams mission, **to remove excuses; specifically surrounding running your application on Linux on Z**. I was responsible for provisioning and supporting 3 production ICP clusters that served as a Content Development portal and hosting utility for around 25 teams at IBM, 200+ people.\nOur goal was to stay current with the releases of ICP so we supported an N-1, N and N+1 configuration where N was the current GA version of ICP. About once a quarter we had to cycle our clusters so quickly I realized that automation was necessary for my own sanity. Using <mark>Terraform</mark> we would interact with <mark>OpenStack</mark> to provision around 10 `s390x` (Z) nodes and 3 `x86` nodes. After the nodes were provisioned I would utilize <mark>Ansible</mark> to configure those nodes with some packages, custom security policies, users and files required for the install.\nPost install I once again utilized Ansible to configure <mark>RBAC</mark> roles for the 25 teams part of the Content Development Clusters. Manually it took about an hour and a half to click through the web-ui, but with Ansible to interact with APIs and a little custom <mark>Python</mark> it only took around 6 minutes running in the background.\nOur team also used these clusters to host and port many different open source applications to Linux on Z. Using Travis on Z I containerized applications like <mark>Jenkins</mark>, <mark>OpenFaaS</mark>, <mark>Postgres</mark>, <mark>Redis</mark>, as well as custom application written in Python and Bash in regression. We use these examples to write public build scripts released by the [Linux on Z](https://github.com/linux-on-ibm-z) outreach team on GitHub.',
     'project_link': 'https://www.ibm.com/cloud/private',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },
     {'title': 'Delete Me3',
     'short_description': 'Delete Me',
     'long_description': 'Delete Me',
     'project_link': 'Delete Me',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },
     {'title': 'Delete Me4',
     'short_description': 'Delete Me',
     'long_description': 'Delete Me',
     'project_link': 'Delete Me',
     'featured': True,
     'tags': 'Kubernetes,Docker'
     },
     {'title': 'Delete Me5',
     'short_description': 'Delete Me',
     'long_description': 'Delete Me',
     'project_link': 'Delete Me',
     'featured': False,
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
            if 'project_link' not in project:
                project_link = ''
            else:
                project_link = project['project_link']
            new_project = Project(
                project['title'],
                project['short_description'],
                project['long_description'],
                project['featured'],
                project_link
            )

            db.session.add(new_project)
            db.session.commit()
            # print(project['title'] + ' commited')

            tags_list = project['tags'].split(',')
            for a_tag in tags_list:
                tag_to_add = Tag.query.filter_by(name=a_tag).first()
                if tag_to_add:
                    project_tag = ProjectTag(project=new_project, tag=tag_to_add)
                    db.session.add(project_tag)
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
