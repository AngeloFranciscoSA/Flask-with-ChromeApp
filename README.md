# Flask-with-ChromeApp
A simple flask code transformed in one "app.exe" and run with ChromeApp

# TO UNDERSTAND THIS PROJECT, YOU NEED TO KNOW, PYTHON AND BASIC HTML!!!
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
      
For PyInstaller you need compile the code on Python 3.X until 3.6 (not working 3.7)
  - pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --icon=favicon.ico app.py
  
        --onefile (create only .exe)
        --windowed (not open cmd viewer)
        --add-data (import the templates and static folders to .exe)
        --icon (just put a icon on your .exe)

Comments:
    
    I use a method to most compact the project is, do all the thing in on page.
    You can create more pages!
    Just using the render_template() and redirect() in FLASK!
    Flask is simple!
