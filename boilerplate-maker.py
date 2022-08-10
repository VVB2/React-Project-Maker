from typing import Optional, List
import os
from rich import print
import typer
import shutil

app = typer.Typer()

client_folders = ['Components', 'Pages', 'Utils', 'Contexts', 'Assets']
server_folders = ['Controllers', 'Helpers', 'Middlewares', 'Models', 'Public']

def react_maker(location, isServer):
    if isServer:
        loc = f'{location}\client'
    else:
        loc = f'{location}'
    for i in client_folders:
        os.mkdir(f'{loc}\src\{i}')
    app_file = open(f'{loc}\src\App.js', 'w')
    app_file.write('''function App() {
return (
    <div>
    Hello World!
    </div>
);
}

export default App;
''')
    app_file.close()
    index_file = open(f'{loc}\src\index.js', 'w')
    index_file.write('''import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />,document.getElementById('root'));
''')
    index_file.close()

@app.command()
def client(name: str, c: Optional[List[str]] = typer.Option([], help="Enter the packages that you need to install."),location: Optional[str] = typer.Option('.', help="Enter the location you want the project to install.")):
    os.system('cls')
    if location != '.':
        loc = f'{location}\{name}'
    else:
        loc = f'{os.getcwd()}\{name}'
    os.chdir(f'{location}')
    os.system(f'npx create-react-app {name}')
    shutil.rmtree(f'{loc}\src', ignore_errors=False, onerror=None)
    os.mkdir(f'{loc}\src')
    react_maker(loc, False)
    os.chdir(f'{name}')
    for package in c:
        os.system('cls')
        print(f'installing [green]{package}[/green]')
        os.system(f'npm install {package}')
    os.system('code .')
    os.system('npm start')

@app.command()
def clientServer(name: str, c: Optional[List[str]] = typer.Option([], help="Enter the packages that you need to install for client."),location: Optional[str] = typer.Option('.', help="Enter the location you want the project to install.")):
    os.system('cls')
    if location != '.':
        loc = f'{location}\{name}'
    else:
        loc = f'{os.getcwd()}\{name}'
    os.mkdir(f'{loc}')
    os.chdir(f'{loc}')
    os.system(f'npx create-react-app client')
    shutil.rmtree(f'{loc}\client\src', ignore_errors=False, onerror=None)
    os.mkdir(f'{loc}\client\src')
    react_maker(loc, True)
    os.chdir('client')
    for package in c:
        os.system('cls')
        print(f'installing [green]{package}[/green]')
        os.system(f'npm install {package}')
    os.system('cls')
    os.chdir(f'..')
    os.system('mkdir server')
    for i in server_folders:
        os.mkdir(f'{loc}\server\{i}')
    os.chdir('server')
    os.system('npm init -y')
    os.system('npm i express mongoose dotenv mongo-sanitize --save')
    os.system('npm i nodemon --save-dev')
    express_file = open(f'{loc}\server\index.js', 'w')
    express_file.write('''const express = require("express");
const morgan = require("morgan");

const app = express();

mongoose
    .connect(process.env.MONGO_URL, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
    }).then(() => {
        console.log(“Database connection Success!”);
    }).catch((err) => {
        console.error(“MongoDB Connection Error”, err);
    });

const PORT = process.env.PORT || 5000; 
app.use(express.json()); 
app.use(morgan("dev"));  
 
app.get("/", (req, res) => {  
  return res.send({
    status: "Healthy",
  });
});
app.listen(PORT, () => {
  console.log("Server started listening on port : ", PORT);
});
''')
    express_file.close()
    os.chdir(f'{loc}')
    os.system('code .')

if __name__ == "__main__":
    app()