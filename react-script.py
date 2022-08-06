from typing import Optional, List
import os
import typer
import shutil

folders = ['Components', 'Pages', 'Utils', 'Contexts', 'Assets']

def create_react_app(name: str, p: Optional[List[str]] = typer.Option([]),location: Optional[str] = 'D:\Projects\Vinod'):
    os.system('cls')
    os.chdir(f'{location}')
    os.system(f'npx create-react-app {name}')
    shutil.rmtree(f'{location}\{name}\src', ignore_errors=False, onerror=None)
    os.mkdir(f'{location}\{name}\src')
    for i in folders:
        os.mkdir(f'{location}\{name}\src\{i}')
    app_file = open(f'{location}\{name}\src\App.js', 'w')
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
    index_file = open(f'{location}\{name}\src\index.js', 'w')
    index_file.write('''import ReactDOM from 'react-dom';
    import App from './App';

    ReactDOM.render(<App />,document.getElementById('root'));
    ''')
    index_file.close()
    os.chdir(f'{name}')
    for package in p:
        os.system(f'echo installing {package}')
        os.system(f'npm install {package}')
    os.system('code .')
    os.system('npm start')

if __name__ == "__main__":
    typer.run(create_react_app)