from app.models import *
from flask import current_app as app

projects=[{'id': 1, 'title': 'KVM Solution Test', 'project_link': 'www.linux-kvm.org/page/Main_Page', 'short_description': '<p>A customer-like solution test for the KVM Hypervisor</p>', 'long_description': '<p>In July of 2020, I stepped into the role of Technical Team Lead for the KVM Solution Test project. When I joined, there was a simple foundation of automation but I quickly identified areas that could be improved . Over the next six months my team and I worked to achieve a goal of 100% automated coverage of the test plan. The team now functions as a mature development organization, evaluating new line items and features as they arise.</p><p>&nbsp;</p><p>We worked with&nbsp; three&nbsp; major Linux distributions (RHEL/SLES/Ubuntu) during their Beta testing periods to verify KVM on their platforms. It was a challenging endeavor maintaining our relationships with 3 different sets of engineers, and I ended up learning a lot from the process about managing priorities and expectations for my team. Where applicable we accommodated large scale testing scenarios <strong>(involving 10TB+ of RAM and 1000+ KVM guests)</strong> which provided a unique value-add to the community, verifying the platform at an enterprise scale.</p><p>&nbsp;</p><p>The DevOps framework was built with Ansible and consisted of <strong>25k+ lines of code.</strong> We approached the framework with an Agile methodology in mind by building an MVP, getting hands on the solution and identifying bugs and innovations. With over 200 pull requests merged to date, we had&nbsp; built an incredible community of contributors extending beyond our immediate team. The power of our collaboration across our test teams built a solid level of resiliency and modularity to the code base, setting the team up for minimal technical debt in the future.</p>', 'featured': True, 'tags': [2, 6, 7, 9, 11, 15, 24], 'achievements': [5], 'collabs': []},{'id': 2, 'title': 'Travis on Z', 'project_link': 'github.com/bendermIBM/travis-cookbooks', 'short_description': '<p>Porting a CICD standard to the Linux on Z platform</p>', 'long_description': '<p>CICD pipelines makes managing the lifecycle and deployment of a product easier and consistent. Travis has a tight integration with GitHub which made it a perfect candidate for internal and open source projects to utilize. For our customers and partners it was a prerequisite to support and run their product on the Z platform.&nbsp;</p><p><br>&nbsp;</p><p>Internally we had a Travis environment for x86 and ppc64le, but none for s390x. I was tasked with supporting Travis on Linux on Z, so began a month-long dive into the source code of Travis learning it from end to end. Utilizing a forked project <a href="https://github.com/bendermIBM/travis-cookbooks">with modifications for s390x</a>, I deployed Travis regression pipeline for the release for IBM Cloud Private (ICP) on Z, a Kubernetes offering by IBM.&nbsp;</p><p>&nbsp;</p><p>In collaboration with my team lead, we built and ported the Travis codebase to `s390x`. Jay focused on the infrastructure, initially hooking OpenStack up to a z/VM hypervisor but ultimately settled on KVM. I focused on the provisioning tools that power the magic of Travis and its integration with GitHub. The code base consisted of Chef cookbooks and custom bash scripts. After three weeks of effort we got our first working build and the result was promising.</p><p>&nbsp;</p><p>For the first time ever our developers were able to modify their Travis pipelines and run their builds on Linux on Z. However as they integrated the s390x builds, all of a sudden Travis on Z became mission critical service due to the nature of Travis and GitHub. If even one architecture failed to pass, Travis integrity checks prevented code from being merged into the main branch. When Travis on Z took an outage, the messages and alerts quickly started flooding in from concerned consumers with deadlines on the horizon. The current solution was not sufficient for a rapidly growing user base.</p><p><br>&nbsp;</p><p>Utilizing load balancing via RabbitMQ we stood up another OpenStack instance located in Hursley, United Kingdom and replicated our port of Travis on Z to those systems. Since then we have been able to take independent outages without affecting an ever growing demand for Travis on Z. However we ran into issues with big bursts of builds which caused the networking layer in Openstack to intermittently not initiate. After days of debugging and testing we abandoned our initial strategy, pivoting to use LXD to run the builds. Ultimately this turned out to be a much better solution, resulting in a huge speed increase and more portability. Using Packer I built<a href="https://github.com/bendermIBM/packer-templates/tree/lxd-templates-travonz"> xenial/bionic base images</a> for Linux on Z and deployed a production configuration supporting 20,000+ builds a year.&nbsp;</p><p>&nbsp;</p><p>Once we moved to the LXD based builds I was able to automate the deployment of LXD and the Travis Worker on a Ubuntu Bionic host using Ansible. Still using the previous OpenStack environment we could now provision infrastructure with Terraform and configure workers in tandem using Ansible.</p>', 'featured': True, 'tags': [1, 6, 14, 17, 19], 'achievements': [4], 'collabs': []},{'id': 3, 'title': 'IBM Cloud Private', 'project_link': 'ibm.com/cloud/private', 'short_description': '<p>IBM Cloud™ Private - a Kubernetes offering on Z</p>', 'long_description': '<p>My team was tasked with supporting and testing IBM Cloud Private (ICP), a Kubernetes offering by IBM, on Linux on Z. Our goal was to have full support by the 3.1.2 release and in order to achieve this we needed to port the Travis project to the Mainframe, as CICD pipelines already existed for other architectures (x86/ppc64le).</p><p>&nbsp;</p><p>Our goal was to stay current with the releases of ICP so we supported an N-1, N and N+1 configuration where N was the current GA version of ICP. About once a quarter we had to cycle our clusters so quickly I realized that automation was necessary. Using Terraform we would interact with OpenStack to provision around a handful of multi-architectural nodes. After the infrastructure was initiated, Ansible was leveraged to install packages, customize security policies, and template required files . The end to end strategy reduced standup time by 70%, a huge success.</p><p>&nbsp;</p><p>Alongside these efforts we saw an opportunity to provide our colleagues with a tool enabling them to run and test their applications in a kubernetes context. I was responsible for provisioning and supporting three&nbsp; production clusters that served as a content development portal and hosting utility for 25+ teams at IBM.&nbsp;<br>&nbsp;</p><p>Our team also used these clusters to host and port many different open source applications to Linux on Z. Using Travis on Z I containerized applications like Jenkins, OpenFaaS, Postgres, Redis, as well as custom applications written in Python and Bash in regression. We use these examples to write public build scripts released by the<a href="https://github.com/linux-on-ibm-z"> Linux on Z</a> outreach team on GitHub.</p>', 'featured': True, 'tags': [1, 3, 6, 7, 8, 9, 10, 11, 23], 'achievements': [4], 'collabs': []},{'id': 4, 'title': 'NexNest', 'project_link': 'github.com/maxbbender/nexnest', 'short_description': '<p>A housing portal for college students</p>', 'long_description': '<p>I had written a couple websites with Flask in college, but wanted to learn more and read up on<a href="https://blog.miguelgrinberg.com/"> Miguel Grinberg</a>\'s Flask tutorial and was exposed to a new set of best practices. Approached with an idea for a rental website targeted at students we designed and implemented a website written in Python. Backed by a fairly complex database that featured notifications and recursive comments, SQLAlchemy handles most of the direct SQL queries the complex `JOIN`s. See the ERD<a href="https://github.com/maxbbender/nexnest/blob/master/docs/erd.pdf"> here</a>.</p><p>&nbsp;</p><p>Building websites has always been a hobby of mine, allowing me a venue for architecting and implementing an idea from the ground up. This project in particular gave me an opportunity to explore modern web frameworks unlike the PHP ones I had worked on before. It\'s great to see frameworks like Laravel, Flask and Django becoming more popular and widely adopted.</p>', 'featured': False, 'tags': [2, 4, 12, 26], 'achievements': [2], 'collabs': []},{'id': 5, 'title': "Let's Talk", 'project_link': None, 'short_description': '<p>A group of educational modules covering a variety of technologies</p>', 'long_description': '<p>Teaching others and seeing the<strong> lightbulb</strong> go off when a concept is realized is a compelling experience for me. In my effort to educate teams at IBM about new Open Source projects I realized that giving the same presentation to team after team was an inefficient method. So I created "Let\'s Talk" which is a group of education modules that have an intense focus on hands-on learning using examples hosted on GitHub. We scheduled live presentations and recorded them for future consumption and they featured code examples accompanied by a tutorial-like presentation.&nbsp;</p><p>&nbsp;</p><p>My main goal with this series was to provide self-sufficient materials for onboarding new-hires and people new to the technology. Hands-on examples were integral for this effort as they gave people the resources &amp; examples they need to get off the ground. External references and documentation were heavily leveraged to demonstrate that all the information is available online.</p><p>&nbsp;</p><p>Some of the Topics : Ansible, Kubernetes, Jenkins, Travis, Python</p>', 'featured': True, 'tags': [1, 3, 5, 6, 15], 'achievements': [4], 'collabs': []},{'id': 7, 'title': 'Viral Education / TALOS', 'project_link': 'github.com/maxbbender/Viral-Education', 'short_description': '<p>TALOS (Textual Augmentation Learning of Semantics), a Web-based platform for vocabulary acquisition that provides capabilities for analytics to support learning of vocabulary.</p>', 'long_description': '<p>The first real website I made for someone other than myself. Written in PHP in a summer alongside working at the Marist College HelpDesk, this website was part of a research project that funded me to present at I<a href="https://iated.org/inted/">NTED</a> in Madrid, Spain. Alongside two professors, I gave a presentation on using technology to enhance learning in an unobtrusive fashion with a concentration in learning foreign languages.</p><p>&nbsp;</p><p>Backed by a MySQL database this is where I learned a lot about security in the modern age of web-development. Certain vulnerabilities such as SQL Injections and XSS were ones that I focused on researching because I knew they were some of the more common avenues of attack.</p>', 'featured': False, 'tags': [7, 8, 13, 21, 26], 'achievements': [2], 'collabs': []},{'id': 8, 'title': 'Bookstore', 'project_link': None, 'short_description': '<p>A java-based customer-like application simulating an Amazon bookstore</p>', 'long_description': '<p>Bookstore was a legacy application when I joined IBM as a co-op that we already had in use in various test plans. There were some improvements that were identified and I was tasked with developing and implementing them. They mainly revolved around data &amp; statistic gathering APIs.</p><p>&nbsp;</p><p>Written mostly in Java, I wrote<a href="https://www.geeksforgeeks.org/introduction-java-servlets/"> Java Servlets</a> which is one of Java\'s web-socket implementations, to serve API requests and respond with formatted data. Still being a student during this project, I had to do a lot of on the fly learning about data manipulation and XML schema rules. Things like characters in different languages or symbols had huge &amp; sometimes disastrous implications to the functionality of an API. Books are written in many languages across the world, and it turns out supporting all of them is a unique challenge. This was my first insight into a development lifecycle at an enterprise like IBM.</p>', 'featured': False, 'tags': [26, 27], 'achievements': [7], 'collabs': []},]

tags=[{'id': 1, 'name': 'Travis', 'knowledge': 'fluent', 'show_on_front': True},{'id': 2, 'name': 'Python', 'knowledge': 'fluent', 'show_on_front': True},{'id': 3, 'name': 'Kubernetes', 'knowledge': 'fluent', 'show_on_front': True},{'id': 4, 'name': 'Flask', 'knowledge': 'fluent', 'show_on_front': True},{'id': 5, 'name': 'Docker', 'knowledge': 'fluent', 'show_on_front': True},{'id': 6, 'name': 'Ansible', 'knowledge': 'fluent', 'show_on_front': True},{'id': 7, 'name': 'Linux', 'knowledge': 'fluent', 'show_on_front': False},{'id': 8, 'name': 'Git', 'knowledge': 'fluent', 'show_on_front': False},{'id': 9, 'name': 'KVM', 'knowledge': 'fluent', 'show_on_front': False},{'id': 10, 'name': 'ElasticSearch', 'knowledge': 'proficient', 'show_on_front': True},{'id': 11, 'name': 'Grafana/Prometheus', 'knowledge': 'proficient', 'show_on_front': True},{'id': 12, 'name': 'SQLAlchemy', 'knowledge': 'proficient', 'show_on_front': True},{'id': 13, 'name': 'PHP', 'knowledge': 'proficient', 'show_on_front': True},{'id': 14, 'name': 'Terraform', 'knowledge': 'proficient', 'show_on_front': True},{'id': 15, 'name': 'Jenkins', 'knowledge': 'proficient', 'show_on_front': True},{'id': 16, 'name': 'Ruby', 'knowledge': 'familiar', 'show_on_front': True},{'id': 17, 'name': 'Packer', 'knowledge': 'familiar', 'show_on_front': True},{'id': 18, 'name': 'AWS', 'knowledge': 'familiar', 'show_on_front': True},{'id': 19, 'name': 'Chef', 'knowledge': 'familiar', 'show_on_front': True},{'id': 20, 'name': 'RabbitMQ', 'knowledge': 'familiar', 'show_on_front': True},{'id': 21, 'name': 'Postgres', 'knowledge': 'familiar', 'show_on_front': True},{'id': 22, 'name': 'Redis', 'knowledge': 'familiar', 'show_on_front': True},{'id': 23, 'name': 'OpenStack', 'knowledge': 'familiar', 'show_on_front': True},{'id': 24, 'name': 'Project-Management', 'knowledge': 'familiar', 'show_on_front': False},{'id': 26, 'name': 'SQL', 'knowledge': 'proficient', 'show_on_front': False},{'id': 27, 'name': 'Java', 'knowledge': 'proficient', 'show_on_front': True},]

project_tags=[{'project_id': 1, 'tag_id': 11},{'project_id': 8, 'tag_id': 27},{'project_id': 1, 'tag_id': 24},{'project_id': 1, 'tag_id': 6},{'project_id': 1, 'tag_id': 2},{'project_id': 1, 'tag_id': 7},{'project_id': 1, 'tag_id': 15},{'project_id': 4, 'tag_id': 2},{'project_id': 4, 'tag_id': 4},{'project_id': 5, 'tag_id': 3},{'project_id': 5, 'tag_id': 5},{'project_id': 5, 'tag_id': 6},{'project_id': 5, 'tag_id': 15},{'project_id': 2, 'tag_id': 6},{'project_id': 2, 'tag_id': 14},{'project_id': 1, 'tag_id': 9},{'project_id': 7, 'tag_id': 7},{'project_id': 7, 'tag_id': 8},{'project_id': 7, 'tag_id': 13},{'project_id': 7, 'tag_id': 21},{'project_id': 3, 'tag_id': 3},{'project_id': 3, 'tag_id': 7},{'project_id': 3, 'tag_id': 23},{'project_id': 3, 'tag_id': 11},{'project_id': 3, 'tag_id': 6},{'project_id': 3, 'tag_id': 9},{'project_id': 3, 'tag_id': 8},{'project_id': 3, 'tag_id': 10},{'project_id': 4, 'tag_id': 12},{'project_id': 4, 'tag_id': 26},{'project_id': 7, 'tag_id': 26},{'project_id': 2, 'tag_id': 1},{'project_id': 2, 'tag_id': 17},{'project_id': 3, 'tag_id': 1},{'project_id': 5, 'tag_id': 1},{'project_id': 2, 'tag_id': 19},{'project_id': 8, 'tag_id': 26},]

collabs=[{'id': 1, 'fname': 'Mike', 'lname': 'Mcginnis', 'clink': None},]

projectcollabs=[]

about_mes=[{'id': 1, 'title': 'Principal Engineer', 'subtitle': 'Curiosity of the Unknown and Unacknowledged', 'description': '', 'quote': ''},]

achievements=[{'id': 2, 'name': 'Marist College', 'start_date': '2014', 'end_date': '2017', 'desc': '<p>Bachelors in Computer Science with a GPA of 3.8 and honors.</p>', 'link': None, 'link_name': None, 'icon': 'fas fa-school', 'order': 10},{'id': 3, 'name': 'Help Desk Operator', 'start_date': '2014', 'end_date': '2015', 'desc': '<p>As you may imagine, working at a Help Desk isn’t glamorous but I gained experience in a skill that would prove to be invaluable. I was resetting passwords and helping people out with basic technology issues, and all that time gaining experience talking with customers. We were on the phone or helping people in person, and looking back on this it set me up with a great foundation for discussing technical concepts with people of all backgrounds.</p>', 'link': 'https://www.marist.edu/', 'link_name': 'Marist', 'icon': 'fas fa-info', 'order': 5},{'id': 4, 'name': 'Principal Test Engineer', 'start_date': 'July 2017', 'end_date': 'July 2020', 'desc': "<p>I started with IBM on the Linux Center of Competence team, focusing on testing Linux on Z and&nbsp;driving open source efforts for the platform. Our team's mission was to remove excuses when it came to running software on Linux on Z which granted me the opportunity to work with some incredibly smart people around the world. Being a vocal contributor put me in a position to work with our customers to modernize workflows and drive net new business to the platform.</p>", 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-server', 'order': 2},{'id': 5, 'name': 'KVM Solution Test Lead', 'start_date': 'July 2020', 'end_date': 'April 2022', 'desc': '<p>As a manager on the KVM Solution test team I led a team of six engineers, collaborating with multi-national colleagues. I leveraged my depth of experience in developer roles to guide the team in transforming our testing strategy by using automation to run 24/7 and achieve 100% test coverage. We primarily leveraged Ansible to manage system configurations across different architectures and deploy network, disk and memory test suites verifying scalability and functionality.&nbsp;<br>&nbsp;</p><p>The leadership position required balancing business requirements and deadlines with technical innovation that would set up our team for success in the future. We worked with three major Linux distribution’s (RHEL/SLES/Ubuntu) engineers to test and verify KVM on their respective operating systems. Ultimately the test cycle length was reduced by 37%, and shift-left by five months to align ourselves with our partner’s beta lifecycles.</p>', 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-server', 'order': 1},{'id': 7, 'name': 'Internship/Co-Op', 'start_date': 'December 2015', 'end_date': 'July 2017', 'desc': "<p>During my time at Marist College, I worked for IBM during the school year and summer. It was a challenge to balance school work with my job's responsibilities but gave a lot of opportunities to practice balancing priorities. I mainly functioned as a developer making updates to various test tools written in Java and Bash.</p>", 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-chalkboard', 'order': 3},]

achievement_projects=[{'project_id': 1, 'achievement_id': 5},{'project_id': 2, 'achievement_id': 4},{'project_id': 3, 'achievement_id': 4},{'project_id': 5, 'achievement_id': 4},{'project_id': 8, 'achievement_id': 7},{'project_id': 4, 'achievement_id': 2},{'project_id': 7, 'achievement_id': 2},]

users=[{'id': 1, 'username': 'bender', 'password_hash': '63d14cd813bf42a0b0c56adeaf5ab36c5d9db009a022027002d3f3bf1f821dbf', 'salt': 'fa34c10f1bda4245b9ab90f9643d7d2b'},] 

def seed_tags(db):
    # ----------------- # 
    # --- Seed Tags --- #
    # ----------------- #
    for tag in tags:
        tag_to_check = Tag.query.filter_by(name=tag['name']).first()
        if not tag_to_check:
            new_tag = Tag(name=tag['name'],
                          knowledge=tag['knowledge'],
                          id=tag['id'],
                          show_on_front=tag['show_on_front'])
            db.session.add(new_tag)
            db.session.commit()
        else:
            app.logger.debug(f'Tag {tag_to_check} already exists')


def seed_projects(db):
    # ----------------- # 
    # - Seed Projects - #
    # ----------------- # 
    for project in projects:
        project_to_check = Project.query.filter_by(title=project['title']).first()

        if not project_to_check:
            new_project = Project(
                title=project['title'],
                short_description=project['short_description'],
                long_description=project['long_description'],
                featured=project['featured'],
                project_link=project['project_link'],
                id=project['id']
            )

            db.session.add(new_project)
            db.session.commit()
        else:
            app.logger.debug(f'Project {project_to_check} already exists')

    # --------------------- # 
    # --- Seed ProjTags --- #
    # --------------------- # 
    for a_tag in project_tags:
        projTag_to_check = ProjectTag.query.filter_by(project_id=a_tag['project_id'], tag_id=a_tag['tag_id']).first()

        if not projTag_to_check:
            project_target = Project.query.filter_by(id=a_tag['project_id']).first()
            tag_target = Tag.query.filter_by(id=a_tag['tag_id']).first()

            newProjTag = ProjectTag(project=project_target, tag=tag_target)
            db.session.add(newProjTag)
            db.session.commit()
        else:
            app.logger.debug(f'project tag {projTag_to_check} already exists')

        
def seed_collabs(db):
    # -------------------- # 
    # --- Seed Collabs --- #
    # -------------------- # 
    for collab in collabs:
        collab_to_check = Collab.query.filter_by(fname=collab['fname'],
                                                 lname=collab['lname']).first()
        if not collab_to_check:
            new_collab = Collab(fname=collab['fname'],
                                lname=collab['lname'],
                                clink=collab['clink'],
                                id=collab['id']
                                )
            db.session.add(new_collab)
            db.session.commit()
        else:
            app.logger.debug(f'Collab {collab_to_check} already exists')

    
    # ------------------------ # 
    # --- Seed ProjCollabs --- #
    # ------------------------ # 
    for projCollab in projectcollabs:
        projCollab_to_check = ProjectCollab.query.filter_by(project_id=projCollab['project_id'], collab_id=projCollab['collab_id']).first()

        if not projCollab_to_check:
            project = Project.query.filter_by(id=projCollab['project_id']).first()
            collab = Collab.query.filter_by(id=projCollab['collab_id']).first()
            newProjCollab = ProjectCollab(project=project, collab=collab)
            db.session.add(newProjCollab)
            db.session.commit()

def seed_aboutme(db):
    # -------------------- # 
    # --- Seed AboutMe --- #
    # -------------------- # 
    for aboutme in about_mes:
        aboutme_check = AboutMe.query.filter_by(title=aboutme['title']).first()
        if not aboutme_check:
            new_aboutme = AboutMe(
                title=aboutme['title'],
                subtitle=aboutme['subtitle'],
                description=aboutme['description'],
                quote=aboutme['quote'],
                id=aboutme['id']
            )
            db.session.add(new_aboutme)
            db.session.commit()
        else:
            app.logger.debug(f'About me {aboutme} already exists')


def seed_achievements(db):
    # ------------------------- # 
    # --- Seed Achievements --- #
    # ------------------------- # 
    for achievement in achievements:
        achievement_check = Achievement.query.filter_by(name=achievement['name'],
                                                        ).first()
        if not achievement_check:
            new_ach = Achievement(
                name=achievement['name'],
                start_date=achievement['start_date'],
                end_date=achievement['end_date'],
                desc=achievement['desc'],
                link=achievement['link'],
                link_name=achievement['link_name'],
                icon=achievement['icon'],
                id=achievement['id'],
                order=achievement['order']
            )
            db.session.add(new_ach)
            db.session.commit()

        else:
            app.logger.debug(f'Achievement {achievement_check} already exists')
        
    # -------------------------------- # 
    # --- Seed AchievementProjects --- #
    # -------------------------------- #

    for achievProject in achievement_projects:
        achieveProj_to_check = AchievementProject.query.filter_by(project_id=achievProject['project_id'], achievement_id=achievProject['project_id']).first()

        if not achieveProj_to_check:
            project_target = Project.query.filter_by(id=achievProject['project_id']).first()
            achievement_target = Achievement.query.filter_by(id=achievProject['achievement_id']).first()
            project_target.achievements.append(achievement_target)
            db.session.commit()
        else:
            app.logger.debug(f'Achievement Project {achievProject} already exists')


def seed_users(db):
    for user in users:
        user_to_check = User.query.filter_by(username=user['username']).first()

        if not user_to_check:
            new_user = User(username=user['username'],
                            password_hash=user['password_hash'],
                            salt=user['salt'])
            db.session.add(new_user)
            db.session.commit()
        else:
            app.logger.debug(f'User {user} already exists')
