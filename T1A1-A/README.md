# Workbook Questions for Part A


ACME Corporation is looking for devs with an understanding of Flask. The following set of questions relate to this RfQ-requirement.

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


## Q4 	Provide an overview and description of a standard source control workflow 100-200


## Q5 	Provide an overview and description of a standard software testing process (e.g. manual testing) 100-200

***
Having suffered several cyber attacks in the past and resultant remedial audits ACME Corporation takes compliance, security and privacy very seriously. The following set of questions relate to this RfQ-requirement.

## Q6 	Discuss and analyse requirements related to information system security and how they relate to the project 100-200


## Q7 	Discuss common methods of protecting information and data and how you would apply them to the project 100-200


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