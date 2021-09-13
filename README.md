# Team Project: Period 5 Children
- [Scrum Board](https://github.com/jeankim05/flask_portfolio/projects/1)
- [Team Insights Graphs](https://github.com/jeankim05/flask_portfolio/graphs/contributors)

Contributor | GitHub | Tasks and Issues | Scrum Board | Commits | Links to Journal
----------- | ----------- | ------------- | ------------- | ------------- | -------------
Jean Kim | [@jeankim05](https://github.com/jeankim05) | [Tasks and Issues](https://github.com/jeankim05/flask_portfolio/issues/assigned/jeankim05) | [Scrum Board](https://github.com/jeankim05/flask_portfolio/projects/1)  | [Commits](https://github.com/jeankim05/flask_portfolio/commits/main?author=jeankim05) |[Jean Kim and Jay Manjrekar Journal](https://docs.google.com/document/d/1bYsR9b6nUoS4Svl8AnUcRA0bOjl8gRcyT-kbd1AhnOc/edit?usp=sharing)
Jay Manjrekar | [@JayManjrekar](https://github.com/JayManjrekar) | [Tasks and Issues](https://github.com/jeankim05/flask_portfolio/issues/assigned/JayManjrekar) | [Scrum Board](https://github.com/jeankim05/flask_portfolio/projects/1) | [Commits](https://github.com/jeankim05/flask_portfolio/commits/main?author=JayManjrekar) | [Jean Kim and Jay Manjrekar Journal](https://docs.google.com/document/d/1bYsR9b6nUoS4Svl8AnUcRA0bOjl8gRcyT-kbd1AhnOc/edit?usp=sharing)
Allie Xiao | [@xiaoa0](https://github.com/xiaoa0) | [Tasks and Issues](https://github.com/jeankim05/flask_portfolio/issues/assigned/xiaoa0) | [Scrum Board](https://github.com/jeankim05/flask_portfolio/projects/1) | [Commits](https://github.com/jeankim05/flask_portfolio/commits/main?author=xiaoa0) | [Allie Xiao and Alex Do Journal](https://docs.google.com/document/d/1M3uMIrhcwQYRoes55MLlfpXWSMjIIvjR96f8v07PCUU/edit?usp=sharing)
Alex Do | [@AlexD017](https://github.com/AlexD017) | [Tasks and Issues](https://github.com/jeankim05/flask_portfolio/issues/assigned/AlexD017) | [Scrum Board](https://github.com/jeankim05/flask_portfolio/projects/1) | [Commits](https://github.com/jeankim05/flask_portfolio/commits/main?author=AlexD017) | [Allie Xiao and Alex Do Journal](https://docs.google.com/document/d/1M3uMIrhcwQYRoes55MLlfpXWSMjIIvjR96f8v07PCUU/edit?usp=sharing)


### Visual thoughts
- Organize with Bootstrap menu 
- Add some color and fun through VANTA Visuals (birds, halo, solar, net)
- Show some practical and fun links (hrefs) like Twitter, Git, Youtube
- Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
- Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
- The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
- The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
- WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
- Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
- The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
- The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
- Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
- The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 
