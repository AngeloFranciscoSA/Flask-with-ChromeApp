# Flask-with-ChromeApp
A simple flask code transformed in one "app.exe" and run with ChromeApp

# TO UNDERSTAND THIS PROJECT, YOU NEED TO KNOW, BASIC PYTHON AND HTML!!!
    I tried to explain everything, but some doubt, go searching is not so complicated!

You need to this project -> Python, Flask, PyInstaller and (pymysql, this for MySQL, you can change this!)

    Your Database, use witch better for you, in this project, I used MySQL. Works with all accept by Python!

    Know the basic in HTML, CSS and JavaScript to use Flask.
     For the Framework:
        - Strongly recommended Jquery and Materialize (I used it in this project)
        - You can change for another, it's your choice!

Tree folder:

    app
      - app.py (main)
      - options.py (settings DB)
      - storage.py (connection with MySQL Database, CRUD)
    
      templates (HTML Template)
        - base.html (base for the Header and footer)
        - index.html (Login)
        - blog.html (Principal page)

      static (stay image)
        - Nothing for now...
    
    venv (so necessary)
     _This is a Virtual Environment on Python!
    
      
For PyInstaller you need compile the code on Python 3.X until 3.6 (not working 3.7)
  - pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --icon=favicon.ico app.py
  
        --onefile (create only .exe)
        --windowed (not open cmd viewer)
        --add-data (import the templates and static folders to .exe)
        --icon (just put a icon on your .exe)
  
# TO RUN:

   *ALL THE STEPS INSIDE COMMAND PROMPT*
   
    Start with venv.
        on your promp, type: "pip install virtualenv" to install.
        next "virtualenv venv", to create.
        active:
            - MAC/OS and LINUX:
                "source venv/bin/activate"
            - Windows:
                "venv\Scripts\activate"
                
    Install all pip extensions.
    
    Inside the folder "app"
        Set up the FLASK APP:
            - Windowns:
                "set FLASK_APP=app.py"

            - Linux and MAC/OS:
                "export FLASK_APP=app.py"

        To start the project:
            - run: "flask run"
        
    Optional:
        to turn flask in the DEBUG mode.
            - This mode will update the code automatically
            
            To turn on DEBUG mode:
                "set FLASK_ENV=development" on windows
                "export FLASK_ENV=development" on LINUX
