# Flask-with-ChromeApp
A simples flask code transform in .exe and run with ChromeApp

You need to this project -> Python, Flask, PyInstaller and pymysql
Know the basic in HTML, CSS and JavaScript (recommended Jquery and Bootstrap or another which framework you perfer)

Tree:

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
