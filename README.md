## **React and MERN Boilerplate Script**
---

> **Motivation** <br />

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
Every programmer knows that staring a new project means spending lot of time to create boilerplates and setting up you project.This script helps you to spend less time on performing redundent tasks and focus on the task which is much more important. <br>
The commands help you to create *react* as well as *MERN* stack projects with just one command.

> **Prerequisites**  
- Python 3.9 or higher
- Pip  
- Git

> **Steps to sucessfully run the script**  
1. Clone this repository <br />
    ```git
    git clone https://github.com/VVB2/React-Project-Maker
    ```

2. Install all the packages <br />
    ```python
    pip install -r requirements.txt
    ```

3. Run any one of the commands <br />
   *For client boilerplate*
    ```python
    python boilerplate-maker.py client [OPTIONS] NAME
    ``` 

    *For MERN boilerplate*
    ```python
    python boilerplate-maker.py clientserver [OPTIONS] NAME
    ```

> **OPTIONS**
- For client and clientserver
    ```
    --c TEXT Enter the packages that you need to install for client.
    --location Enter the location you want the project to install. [default: .]
    --help Help about this command
    ```

> **Note** <br />
- *The NAME is required to run the script for both client and server commands* 
- *To install multiple dependencies seperate each dependency with **--c** tag*
- *In the **clientserver** command the default packages installed are **express mongoose dotenv mongo-sanitize** and **nodemon** as dev-dependencies*

> **The folder structure generated is as follows**
- For client
    ```
    <NAME>
    ┣ node_modules
    ┣ public
    ┃ ┣ favicon.ico
    ┃ ┣ index.html
    ┃ ┣ logo192.png
    ┃ ┣ logo512.png
    ┃ ┣ manifest.json
    ┃ ┗ robots.txt
    ┣ src
    ┃ ┣ Assets
    ┃ ┣ Components
    ┃ ┣ Contexts
    ┃ ┣ Pages
    ┃ ┣ Utils
    ┃ ┣ App.js
    ┃ ┗ index.js
    ┣ .gitignore
    ┣ package-lock.json
    ┣ package.json
    ┗ README.md
    ```

- For clientserver
   ```
    <NAME>
    ┣ client
    ┣ node_modules
    ┃ ┣ public
    ┃ ┃ ┣ favicon.ico
    ┃ ┃ ┣ index.html
    ┃ ┃ ┣ logo192.png
    ┃ ┃ ┣ logo512.png
    ┃ ┃ ┣ manifest.json
    ┃ ┃ ┗ robots.txt
    ┃ ┣ src
    ┃ ┃ ┣ Assets
    ┃ ┃ ┣ Components
    ┃ ┃ ┣ Contexts
    ┃ ┃ ┣ Pages
    ┃ ┃ ┣ Utils
    ┃ ┃ ┣ App.js
    ┃ ┃ ┗ index.js
    ┃ ┣ .gitignore
    ┃ ┣ package-lock.json
    ┃ ┣ package.json
    ┃ ┗ README.md
    ┗ server
    ┃ ┣ Controllers
    ┃ ┣ Helpers
    ┃ ┣ Middlewares
    ┃ ┣ Models
    ┃ ┣ Public
    ┣ node_modules
    ┃ ┣ index.js
    ┃ ┣ package-lock.json
    ┃ ┗ package.json
   ```


