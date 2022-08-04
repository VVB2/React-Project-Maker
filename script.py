import os
import sys
import shutil

os.system('cls')

n = len(sys.argv)
folders = ['Components', 'Pages', 'Utils', 'Contexts', 'Assets']

os.system(f'npx create-react-app {sys.argv[1]}')

os.chdir(f'{sys.argv[1]}')

if n>=2:
    for i in range(2,n):
        os.system(f'echo installing {sys.argv[i]}')
        os.system(f'npm install {sys.argv[i]}')

shutil.rmtree('src', ignore_errors=True)
os.mkdir(f'D:/Projects/Vinod/{sys.argv[1]}/src')

for i in folders:
    os.mkdir(f'D:/Projects/Vinod/{sys.argv[1]}/src/{i}')

app_file = open(f'D:/Projects/Vinod/{sys.argv[1]}/src/App.js', 'w')
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

index_file = open(f'D:/Projects/Vinod/{sys.argv[1]}/src/index.js', 'w')
index_file.write('''import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />,document.getElementById('root'));
''')
index_file.close()

os.system('code .')
os.system('npm start')
