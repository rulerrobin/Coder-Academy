# Workbook Questions for Part A

## Q1 	Describe the architecture of a typical Flask application 200-300
Flask application usually consists of a simple architecture known as the Model-View-Controller pattern or framework. With this information we can see that it is divded into three parts with their own roles in an application.

**The Model**

The model holds the data and business logic of the Flask app and usually it would include the data or classes that control or provide the structure of the data. The model would also be the one that actually talks to other databases to retrieve or modify data. Some things that can be used are SQLAlchemy and Flask-SQLAlchemy to interact with databases in Flask applications.

**The View**

The view is what is presented to the client and is responsible for the requests of the user. As an example this could be what built a website such as the interface by CSS and HTML. After user requests are sent they are then sent to the controller.

**The Controller**

The controller acts as a middle man between the model and the view what it does is acts as the processor of information. When the request is sent from the view it then processes the information with help from the model and updates the view as needed. The controller in flask is used by routes and assisted/defined by using decorators such as `@app.route("/")`. This mapping is used to link different routes to different functions in Python. The controller can also be used for authentication, authorization, validation and error handling through decorators such as `@jwt_required()`


Flask Documentation: https://flask.palletsprojects.com/
Pallets Projects: https://palletsprojects.com/
Coder Academy Slides and Information through ntoes

## Q2 	Identify a database management system (DBMS) commonly used in web applications (including Flask) and discuss the pros and cons of this database 150-250

A DMBS that is widely used in web applications including Flask is PSQL which has pros and cons.

**Pros**

The reliability of PSQL is quite well known and ensures that it is a reliable choice for web applications. It has a wide array of features that can be used for simple and complex queries with a plus of being agnostic in regards to programming languages meaning that it is widely supported and has a large library of usable extensions and support.

If built well PSQL is able to handle applications and datasets that are scaling or already large quite well due to its optimisation and caching making it quite an efficient workhorse. In use where multiple transactions need to complete, the data can be simultaneously completed without interfering with each other ensuring data integrity as well.

**Cons**

While PSQL is known for its variety of features and flexibility this can also be con because it can be a bit more complex to set up if only a simpler DBMS can be used isntead. Otherwise instead of efficiency it might work slower and will need to be rebuilt later on for scalability. This can also cause memory issues when scaled up because PSQL can require careful tuning to ensure that the memory usage is done correct in the first place. 

PostgreSQL: a closer look at the object-relational database management system  https://www.ionos.com/digitalguide/server/know-how/postgresql/

What is PostgreSQL? https://www.guru99.com/introduction-postgresql.html
***
ACME Corporation is very big on project management, documentation and process. This will be a key metric in their decision to award the project. The following set of questions relate to this RfQ-requirement.

## Q3 	Discuss the implementation of Agile project management methodology 200-300

Agile project management is a methodology that invites a collaborative effort that focuses on flexibility and customer satisfaction. The focus is to create small frequent changes with continues feedback on these changes which then iterate and iterate until a project is successfully completed. It promotes a close relationship between stakeholders and teams allowing a quick response to change with a mindset focused on adaptability.

An example of a framework is called Scrum which is a method that dives the project in "sprints", typically there are daily meetings for progress udpates and a review done at each end of the sprint with reviews of what happened. This type of methodology promotes continuous progress and improvement whilst also allowing adaptation to any feedback with daily standups and reviews of sprints.

Between the team members and the stakeholders, this style of management is possible because of what is known as the "project backlog", which is a set of features, needs, requirements that are and are being priortised. This list due to the agile methodology is being constantly updated with what is needed. By doing this in theory software can be delivered earlier and more frequently/

At the heart of it all, Agile project management methodologies is a flexible and adaptive style of management that focuses on assisting with teams to consistently adapt to any changing requirements that are needed or removed through feedback and customer value. It allows requirements to evolve as needed and delivers successful projects through a style of iteration and collaboration.

What Is Agile Methodology in Project Management? https://www.wrike.com/project-management-guide/faq/what-is-agile-methodology-in-project-management/

Beginner’s Guide to Agile Project Management https://business.adobe.com/blog/basics/agile

## Q4 	Provide an overview and description of a standard source control workflow 100-200

A standard source control workflow used is called the branch workflow. This type of workflow a new feature or task is separated from the others and made into it's own "branch" and then once completed will merge it back into the main database of code. This workflow helps to keep the main database of code clean and stable as many developers may be working on different projects all at once as well as being able to assist each other thing things such as pull requests.

In the branch workflow it usually involves the following steps:
1. Branch Creation: New branch is made for feature or task
2. Development: Changes are made and commited to their code to test
3. Pull Request: Feature is completed and is sent of to check and review changes
4. Code Review: Other members check the code before signing off
5. Merge: If code is apporved the branch is merged back into branch for a enw feature in the codebase
6. Testing: Tests are compelted to ensure that this change is not causing/has not caused any issues.
7. Deployment: Code is sent into production(sent to be used by clients)

Git Feature Branch Workflow  https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow

## Q5 	Provide an overview and description of a standard software testing process (e.g. manual testing) 100-200

The standard software testing process is a systematic approach that has mutliple sages to identity, assess and check the software follows the requirements set out.

In general the steps taken for testing is usually:

1. Planning: The process starts with planning tests that can check if the software meets the requirements with test cases, testables and scope.
2. Design: After the plan is completed tests are made based on the plans such as expected outputs, inputs, and how to complete a test.
3. Implementation: Test designs are implemented watching the requirements vs the actual results which can include defects or bugs.
4. Error Handling: Any bugs are reported and set as a priority of fixing which are then fixed.
5. Completion and Reporting: Test results are documented and bugs are all adressed.

Through following a standard software testing process software development teams are able to find and assess defects, errors, bugs and unexpected results in software functionality. They are also able to determine if the software meets the minimum requirements and therefore also should be able to provide a high qulaity product that satisfies client expectations.

A Brief Guide to Software Testing - Standards and Processes https://www.specbee.com/blogs/software-testing-standards-and-processes

Fundamentals of Software Testing: Concepts and Process https://www.simplilearn.com/tutorials/devops-tutorial/fundamentals-of-software-testing

***
Having suffered several cyber attacks in the past and resultant remedial audits ACME Corporation takes compliance, security and privacy very seriously. The following set of questions relate to this RfQ-requirement.

## Q6 	Discuss and analyse requirements related to information system security and how they relate to the project 100-200

In regards to the project since it is for a product line that will be sold to customers the minimum requirements of security for this would be to protect;

1. Customer data
2. Confidentiality
3. System integrity

It is crucual that data privacy is secure especially in complience with the data protection regulations. This would involve appropriate security measures such as secure data storage, encryption and access controls as data breaches and unathorised access needs to be protected from. With this a secure way to identify a user must be in place whether it be for user or admin for example requiring two factor authentication or password policies or lockouts.

HTTPS should be employed if possible as it's a secure communication protocol to ensure any data transferred is done properly and securely, this can be enhanced using encryption technology such as the SSL security protocol. Furthermore since this is an application for a product line there needs to be a secure payment method in accordance with the global standard of the Payment Card Industry Data Security Standard. 


## Q7 	Discuss common methods of protecting information and data and how you would apply them to the project 100-200

Following from the above mentioned information some common methods of protecting information and data are:

1. Encryption: Encryption would be very important in order to protect the very basic needs of the application because only those with the encryption key are able to decipher it. This would help protect data confidentiality with client, data, company and customers.
2. Access Controls: Through having access control options this makes it so that only those who have the correct access are able to access different information, whether it be publicy avalilable or sensitive private data that should only be available to those with the appropriate access control. A simple example of this being used are customers logging into the application and requesting them to have mutli factor authentication or a strong password that is not easily accessible.
3. Regular Updates: A basic implementation to protect informtion and data is to simply keep up to date with the latest verions and protections needed to protect against vulnerabilities and exploits. A regular patch will allow the software used to keep out any found from the previous version.

11 Web Application Security Best Practices You Need to Know https://www.mobindustry.net/blog/11-web-application-security-best-practices-you-need-to-know/

10 Web Application Security Best Practices to Secure Your Data https://www.dailyrazor.com/blog/10-web-application-security-best-practices-to-secure-your-data/

6 Essential Data Protection Methods https://gdprinformer.com/gdpr-articles/6-essential-data-protection-methods

## Q8   Research what your legal obligations are in relation to handling user data and how they can be met for the project

***
ACME Corporation has specifically requested the app to be based on a relational database. The next set of questions relate to this RfQ-requirement.

## Q9 	Describe the structural aspects of the relational database model. Your description should include information about the structure in which data is stored and how relations are represented in that structure. 	100-200

## Q10 	Describe the integrity aspects of the relational database model. Your description should include information about the types of data integrity and how they can be enforced in a relational database. 	100-200

## Q11 	Describe the manipulative aspects of the relational database model. Your description should include information about the ways in which data is manipulated (added, removed, changed, and retrieved) in a relational database. 	100-200


***
Companies (including ACME Corporation) value previous project experience and case studies. The following set of questions relate to this RfQ-requirement. 

## Q12 	Conduct research into a web application (app) and answer the following parts:  a. List and describe the software used by the app.
  b. Describe the hardware used to host the app.
  c. Describe the interaction of technologies within the app
  d. Describe the way data is structured within the app
  e. Identify entities which must be tracked by the app
  f. Identify the relationships and associations between the entities you have identified in part (e)
  g. Design a schema using an Entity Relationship Diagram (ERD) appropriate for the database of this website (assuming a relational database model) 	50-100 per part