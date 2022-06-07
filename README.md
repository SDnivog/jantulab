Step - 1 : Activate virtual env  : source jantulab_env/bin/activate
Step - 2 : Install dependencies : pip install -r requirements.txt
Step - 3 : Run App : uvicorn main:app --reload  (at development)

Table Fields : 
1. For Student : table name = User
                 fields ['id','name','email','password']

2. For Books : table name = Book
                 fields ['id','title','description','user_id']



Project Structure :

(a). Admin  -----------------[Library Management]---------------(b). Student

Register : 1. Register with diffrent role in same Table  OR
           2. Register in diffrent Tables

Login :    1. Login from same table with role  OR
           2. Login from two diffrents tables

(a). Admin: 

Role : Add books [CRUD operation]
       Add Inventry [CRUD operation]
       Access all Students Informations [Active/InActive Student]

(b). Student:

Role : Issue Books
       Return Books
       Update My personal Informations

       
              

Note : I attempted to incorporate considerations because task completion takes longer.

I have implemented login auth, CRUD operation


