from app.models import *
from flask import current_app as app

projects=[{'id': 1, 'title': 'KVM Solution Test', 'project_link': 'www.linux-kvm.org/page/Main_Page', 'short_description': '<p>A customer-like solution test for the KVM Hypervisor</p>', 'long_description': '<p>Back in July of 2020, I took over the role as a Technical Team Lead for the KVM Solution Test project. When I joined, there were was a foundation of automation but I quickly identified areas that could be improved on. Over the next 6 months my team and I worked to achieve a goal of 100% automated coverage of the test cases we were responsible for. We have achieved that goal and now are functioning as a mature development organization, evaluating new line items/features as they arise and have begun the process to modularlize &amp; externalize our environment.</p><p><br>We worked with the 3 major Linux distributions (RHEL/SLES/Ubuntu) during their Beta testing periods to verify KVM on their platforms. It was a challenging endeavor maintaining our relationships with 3 different sets of engineers, but I ended up learning a lot from the process about managing priorities and expectations for my team. Where applicable we accommodated large scale testing scenarios <strong>(involving 10TB+ of RAM or 1000+ KVM guests)</strong> which provided a unique value-add to the community, verifying the platform at an enterprise scale.</p><p><br>The DevOps framework was built with Ansible and consisted of <strong>25k+ lines of code.</strong> We approached the framework with an Agile methodology in mind by building an MVP, getting hands on the solution in order to identify the next required evolution. It is going great with over 200 pull requests merged to date, and many more new ones currently open. The power of our collaboration across the team has built in an incredible level of resiliency to the code base, setting the team up to continue to innovate for years to come.</p>', 'featured': True, 'tags': [2, 6, 11, 15, 9, 24, 7], 'achievements': [5], 'collabs': []},{'id': 8, 'title': 'Bookstore', 'project_link': None, 'short_description': '<p>A java-based customer-like application simulating an Amazon bookstore</p>', 'long_description': '<p>Bookstore was a legacy application when I joined IBM as a co-op that we already had in use in various test plans. There were some improvements that were identified and I was tasked with developing and implementing those improvements. They mainly revolved around data &amp; statistic gathering APIs.</p><p>&nbsp;</p><p>Written mostly in Java, I wrote <a href="https://www.geeksforgeeks.org/introduction-java-servlets/">Java Servlets</a> which is one of Java\'s web-socket implementations, to serve API requests and respond with formatted data. Still being a student during this project, I had to do a lot of on the fly learning about data manipulation and XML schema rules. Things like characters in different languages or symbols had huge &amp; sometimes disastrous implications to the functionality of an API. Books are written in many languages across the world, and it turns out supporting all of them is a challenge! Lots of good learning all around and was my first insight into a development lifecycle at an enterprise like IBM.</p>', 'featured': False, 'tags': [27], 'achievements': [7], 'collabs': []},{'id': 2, 'title': 'Travis on Z', 'project_link': 'github.com/bendermIBM/travis-cookbooks', 'short_description': '<p>Enabling the CICD that enables the tools - on Linux on Z</p>', 'long_description': '<p>A big part of my voyage in OpenSource has been learning how to use CICD tools to build automation around a product. For me it was a necessity, because the tediousness of re-running builds had gotten to vast. Travis offers a free CICD mechanism hooked natively into GitHub and many of the projects I was looking at were using it in their pipelines.&nbsp;</p><p>&nbsp;</p><p>Internally we had a Travis environment for x86 and ppc64le, but none for s390x. I was tasked with supporting Travis on Linux on Z and so began a month dive into the source code of Travis. With this we were able to enable a regression pipeline for the release for IBM Cloud Private (ICP) on Z, a Kubernetes offering by IBM.&nbsp;</p><p>&nbsp;</p><p>In collaboration with my team lead and STSM @ IBM, Jay Brenneman, we built and ported the Travis codebase to `s390x`. Jay focused on the hypervisor end, initially hooking OpenStack up to z/VM and eventually moving to KVM on Linux on Z. Meanwhile I focused on the provisioning tools that largely make up the magic of Travis. Largely this consisted of Chef cookbooks and custom bash scripts and took some 3 weeks to get our first working build, but it was glorious.&nbsp;</p><p>&nbsp;</p><p>For the first time ever our developers were able to modify their Travis pipelines and run their builds on Linux on Z. However as they integrated the s390x builds, all of a sudden Travis on Z became mission critical to all of ICP development due to the nature of Travis and GitHub. If even one architecture fails to pass, Travis will block code from being merged into the master branch. When Travis on Z took an outage, the messages and alerts quickly started flooding in. After our second extended outage we quickly realized that we had to come up with a highly available solution for the tool.</p><p>&nbsp;</p><p>Utilizing a load balancing feature in RabbitMQ we stood up another OpenStack instance located in Hursley, United Kingdom and replicated our port of Travis on Z to those systems. Since then we have been able to take independent outages without affecting an ever growing demand for Travis on Z.</p><p>&nbsp;</p><p>&nbsp;</p><p>— &nbsp;Extra Info</p><p>It began with connecting the <a href="https://github.com/travis-ci/worker/network/members">travis-ci worker</a> to an Openstack instance hosted on z/KVM. However we ran into issues with big bursts of builds which caused the networking layer in Openstack to intermittently not initiate. Eventually we upgraded to use LXD to run the builds which gave a huge speed increase and more portability. Using Packer I built <a href="https://github.com/bendermIBM/packer-templates/tree/lxd-templates-travonz">xenial/bionic base images</a> for Linux on Z and deployed a production configuration supporting 20,000+ builds a year. See some changes to the <a href="https://github.com/bendermIBM/travis-build">travis-build scripts</a> which also needed some configurations</p><p>&nbsp;</p><p>Once I moved to the LXD based builds I was able to automate the deployment of LXD and the Travis Worker on a Ubuntu Bionic host using Ansible. Still using the previous OpenStack environment we could now provision infrastructure with Terraform and configure workers using Ansible.</p>', 'featured': True, 'tags': [5, 6, 14], 'achievements': [4], 'collabs': []},{'id': 4, 'title': 'NexNest', 'project_link': 'github.com/maxbbender/nexnest', 'short_description': '<p>A housing portal for college students</p>', 'long_description': '<p>I had written a couple websites with Flask in school, but wanted to learn more and read up on <a href="https://blog.miguelgrinberg.com/">Miguel Grinberg</a>\'s Flask tutorial and was exposed to a new set of best practices. Approached with an idea for a rental website targeted at students we designed and implemented a website written in Python. Backed by a fairly complex database that featured notifications and recursive comments, SQLAlchemy handles most of the direct SQL queries the complex `JOIN`s. See the ERD <a href="https://github.com/maxbbender/nexnest/blob/master/docs/erd.pdf">here</a>.</p><p>&nbsp;</p><p>Building websites scratches my itch for creativity, allowing me a venue for architecting and implementing an idea from the ground up. This project in particular gave me an opportunity to explore modern web frameworks unlike the PHP ones I had worked on before. It\'s great to see frameworks like Laravel, Flask and Django becoming more popular and widely adopted.&nbsp;</p>', 'featured': False, 'tags': [2, 4, 12, 26], 'achievements': [3], 'collabs': []},{'id': 5, 'title': "Let's Talk", 'project_link': None, 'short_description': '<p>A group of educational modules covering a variety of technologies</p>', 'long_description': '<p>Teaching others and seeing that<strong> lightbulb</strong> go off is and experience that I get a lot of gratification from. In my effort to educate teams at IBM I realized that giving the same presentation to team after team was an inefficient method. So I created "Let\'s Talk" which is a group of education modules that have an intense focus on hands-on learning using examples hosted on GitHub. We scheduled live presentations and recorded them for future consumption and they featured code examples accompanied by a tutorial-like presentation.&nbsp;</p><p>&nbsp;</p><p>My main goal with this series was to provide self-sufficient materials for onboarding new-hires and people new to the technology. Hands-on examples were integral for this effort as they gave people the resources &amp; examples they need to get off the ground. External references and documentation were heavily leveraged to demonstrate that all the information is available online, you just need to know where to look.&nbsp;</p><h2>&nbsp;</h2><h2>Education Modules</h2><p>1. Ansible</p><p>2. Kubernetes</p><p>3. Jenkins</p><p>4. Travis</p><p>5. Python</p><p>&nbsp;</p><p>&nbsp;</p>', 'featured': True, 'tags': [3, 5, 6, 15], 'achievements': [4], 'collabs': []},{'id': 7, 'title': 'Viral Education / TALOS', 'project_link': 'github.com/maxbbender/Viral-Education', 'short_description': '<p>TALOS (Textual Augmentation Learning of Semantics), a Web-based platform for vocabulary acquisition that provides capabilities for analytics to support learning of vocabulary.</p>', 'long_description': '<p>The first real website I made for someone other than myself. Written in PHP in a summer alongside working at the Marist College HelpDesk, this website was part of a research project that funded me to present at I<a href="https://iated.org/inted/">NTED</a> in Madrid, Spain. Alongside two professors, I gave a presentation on using technology to enhance learning in an un-obtrusive fashion with a concentration in learning foreign language</p><p>&nbsp;</p><p>Backed by a MySQL database this is where I learned a lot about security in the modern age of web-development. Certain vulnerabilities such as SQL Injections and XSS were ones that I focused on researching because I knew they were some of the more common avenues of attack. Looking back on it however I have already noticed some mistakes but I was happy with how it came out.</p>', 'featured': False, 'tags': [13, 21, 7, 8, 26], 'achievements': [3], 'collabs': []},{'id': 3, 'title': 'IBM Cloud Private', 'project_link': 'ibm.com/cloud/private', 'short_description': '<p>IBM Cloud™ Private - a Kubernetes offering on Z</p>', 'long_description': '<p>My team was tasked with supporting a release of IBM Cloud Private (ICP), a Kubernetes offering by IBM, on Linux on Z. Our goal was to have full support by the 3.1.2 release and to do this we ported Travis to the Mainframe as mentioned above.&nbsp;</p><p>&nbsp;</p><p>Alongside these efforts we saw an opportunity to further drive our teams mission, to remove excuses; specifically surrounding running your application on Linux on Z. I was responsible for provisioning and supporting 3 production ICP clusters that served as a Content Development portal and hosting utility for around 25 teams at IBM, 200+ people.&nbsp;</p><p>&nbsp;</p><p>Our goal was to stay current with the releases of ICP so we supported an N-1, N and N+1 configuration where N was the current GA version of ICP. About once a quarter we had to cycle our clusters so quickly I realized that automation was necessary for my own sanity. Using Terraform we would interact with OpenStack to provision around 10 s390x (Z) nodes and 3 `x86` nodes. After the nodes were provisioned I would utilize Ansible to configure those nodes with some packages, custom security policies, users and files required for the install.</p><p>&nbsp;</p><p>Post install I once again utilized Ansible to configure RBAC roles for the 25 teams part of the Content Development Clusters. Manually it took about an hour and a half to click through the web-ui, but with Ansible to interact with APIs and a little custom Python it only took around 6 minutes running in the background.&nbsp;</p><p>&nbsp;</p><p>Our team also used these clusters to host and port many different open source applications to Linux on Z. Using Travis on Z I containerized applications like Jenkins, OpenFaaS, Postgres, Redis, as well as custom application written in Python and Bash in regression. We use these examples to write public build scripts released by the <a href="https://github.com/linux-on-ibm-z)">Linux on Z</a> outreach team on GitHub.</p>', 'featured': True, 'tags': [3, 6, 11, 23, 9, 7, 8, 10], 'achievements': [4], 'collabs': []},]

tags=[{'id': 11, 'name': 'Grafana/Prometheus', 'knowledge': 'proficient', 'show_on_front': True},{'id': 27, 'name': 'Java', 'knowledge': 'proficient', 'show_on_front': True},{'id': 24, 'name': 'Project-Management', 'knowledge': 'familiar', 'show_on_front': False},{'id': 6, 'name': 'Ansible', 'knowledge': 'fluent', 'show_on_front': True},{'id': 5, 'name': 'Docker', 'knowledge': 'fluent', 'show_on_front': True},{'id': 2, 'name': 'Python', 'knowledge': 'fluent', 'show_on_front': True},{'id': 7, 'name': 'Linux', 'knowledge': 'fluent', 'show_on_front': False},{'id': 15, 'name': 'Jenkins', 'knowledge': 'proficient', 'show_on_front': True},{'id': 4, 'name': 'Flask', 'knowledge': 'fluent', 'show_on_front': True},{'id': 3, 'name': 'Kubernetes', 'knowledge': 'fluent', 'show_on_front': True},{'id': 14, 'name': 'Terraform', 'knowledge': 'proficient', 'show_on_front': True},{'id': 9, 'name': 'KVM', 'knowledge': 'fluent', 'show_on_front': False},{'id': 8, 'name': 'Git', 'knowledge': 'fluent', 'show_on_front': False},{'id': 13, 'name': 'PHP', 'knowledge': 'proficient', 'show_on_front': True},{'id': 21, 'name': 'Postgres', 'knowledge': 'familiar', 'show_on_front': True},{'id': 23, 'name': 'OpenStack', 'knowledge': 'familiar', 'show_on_front': True},{'id': 10, 'name': 'ElasticSearch', 'knowledge': 'proficient', 'show_on_front': True},{'id': 12, 'name': 'SQLAlchemy', 'knowledge': 'proficient', 'show_on_front': True},{'id': 26, 'name': 'SQL', 'knowledge': 'proficient', 'show_on_front': False},{'id': 20, 'name': 'RabbitMQ', 'knowledge': 'familiar', 'show_on_front': True},{'id': 17, 'name': 'Packer', 'knowledge': 'familiar', 'show_on_front': True},{'id': 18, 'name': 'AWS', 'knowledge': 'familiar', 'show_on_front': True},{'id': 19, 'name': 'Chef', 'knowledge': 'familiar', 'show_on_front': True},{'id': 16, 'name': 'Ruby', 'knowledge': 'familiar', 'show_on_front': True},{'id': 1, 'name': 'Travis', 'knowledge': 'fluent', 'show_on_front': True},{'id': 22, 'name': 'Redis', 'knowledge': 'familiar', 'show_on_front': True},]

project_tags=[{'project_id': 1, 'tag_id': 11},{'project_id': 8, 'tag_id': 27},{'project_id': 1, 'tag_id': 24},{'project_id': 1, 'tag_id': 6},{'project_id': 2, 'tag_id': 5},{'project_id': 1, 'tag_id': 2},{'project_id': 1, 'tag_id': 7},{'project_id': 1, 'tag_id': 15},{'project_id': 4, 'tag_id': 2},{'project_id': 4, 'tag_id': 4},{'project_id': 5, 'tag_id': 3},{'project_id': 5, 'tag_id': 5},{'project_id': 5, 'tag_id': 6},{'project_id': 5, 'tag_id': 15},{'project_id': 2, 'tag_id': 6},{'project_id': 2, 'tag_id': 14},{'project_id': 1, 'tag_id': 9},{'project_id': 7, 'tag_id': 7},{'project_id': 7, 'tag_id': 8},{'project_id': 7, 'tag_id': 13},{'project_id': 7, 'tag_id': 21},{'project_id': 3, 'tag_id': 3},{'project_id': 3, 'tag_id': 7},{'project_id': 3, 'tag_id': 23},{'project_id': 3, 'tag_id': 11},{'project_id': 3, 'tag_id': 6},{'project_id': 3, 'tag_id': 9},{'project_id': 3, 'tag_id': 8},{'project_id': 3, 'tag_id': 10},{'project_id': 4, 'tag_id': 12},{'project_id': 4, 'tag_id': 26},{'project_id': 7, 'tag_id': 26},]

collabs=[{'id': 1, 'fname': 'Mike', 'lname': 'Mcginnis', 'clink': None},]

projectcollabs=[]

about_mes=[{'id': 1, 'title': 'Principal Engineer', 'subtitle': 'Curiosity of the Unknown and Unacknowledged', 'description': '', 'quote': ''},]

achievements=[{'id': 5, 'name': 'KVM Solution Test Lead', 'start_date': 'July 2020', 'end_date': 'April 2022', 'desc': "<p>In July I took over a new position as a technical team lead for the KVM Solution test project with a team of 5 people. This position's responsibilities mainly revolved around project management but also involved architecting a new automation framework to achieve our goal of 100% automation coverage. Working on KVM (a Linux hypervisor) we utilized Ansible to manage system configurations as it is a very powerful tool due to the idempotency it implements.&nbsp;</p><p>&nbsp;</p><p>While in the position, I learned a lot about how to balance business requirements &amp; deadlines with neccesary technical innovation. We worked with the 3 major Linux distributions (RHEL/SLES/Ubuntu) engineers to test &amp; verify KVM on their platform, so there was a lot of external deadlines &amp; processes I had to take into account with our test plan. Since starting this position I have helped reduce our overall test cycle length by 25% and shifted it to be 5+ months earlier by leveraging the previously mentioned end to end automation framework built to verify KVM on Z.</p>", 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-server', 'order': 1},{'id': 7, 'name': 'Internship/Co-Op', 'start_date': 'December 2015', 'end_date': 'July 2017', 'desc': "<p>During my schooling at Marist College, I worked for IBM during the school year and summer. It was a challenge to balance school work with my job's responsibilities but gave me a lot of opportunities to practice balancing priorities from different sources. I learned a lot during this experience, and it gave me a great jumpstart into my future career at IBM</p>", 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-chalkboard', 'order': 3},{'id': 4, 'name': 'Principal Test Engineer', 'start_date': 'July 2017', 'end_date': 'July 2020', 'desc': "<p>My first full time career at IBM was on the Linux Center of Competence team which focused on testing Linux on Z with a similar context as my internship. &nbsp;Part of the team's mission was to remove excuses when it came to running software on Linux on Z. I had the chance to work and architect many different CICD solutions, and participated in workshops with our customers, advocating open source software solutions on the Z platform.</p>", 'link': 'https://www.ibm.com/us-en/', 'link_name': 'IBM', 'icon': 'fas fa-server', 'order': 2},{'id': 3, 'name': 'Help Desk Operator', 'start_date': '2014', 'end_date': '2015', 'desc': '<p>While my time at the Help Desk wasn’t the most glamorous, I valued it a lot. I was resetting passwords and helping people out with basic technology issues but during that I was gaining so much experience in talking with customers. We were on the phone or helping people in person and looking back on it this experience has strengthened my ability to interact with customers in the field.</p>', 'link': 'https://www.marist.edu/', 'link_name': 'Marist', 'icon': 'fas fa-info', 'order': 5},{'id': 2, 'name': 'Marist College', 'start_date': '2014', 'end_date': '2017', 'desc': '<p>Graduated with a bachelors in Computer Science with GPA of 3.8 and honors. During my time at Marist I participated in the MCCS and many other community activities which strengthend my value as a teammate and leader.&nbsp;</p>', 'link': None, 'link_name': None, 'icon': 'fas fa-school', 'order': 10},]

achievement_projects=[{'project_id': 1, 'achievement_id': 5},{'project_id': 2, 'achievement_id': 4},{'project_id': 3, 'achievement_id': 4},{'project_id': 5, 'achievement_id': 4},{'project_id': 4, 'achievement_id': 3},{'project_id': 7, 'achievement_id': 3},{'project_id': 8, 'achievement_id': 7},] 

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
