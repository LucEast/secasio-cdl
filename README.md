# secasio-cdl

## Script Setup

```
# Create venv 
python3 -m venv /path/to/venv

# Run Powershell as an Administrator 
Set-ExecutionPolicy Unrestricted (Optional - Disables needs of Admin privileges)

# Activate venv: Windows
.\path\to\venv\Scripts\Activate.ps1

# Activate venv: Linux / MacOS
source venv/bin/activate

# Install requirements directly
pip3 install inquirer
pip3 install requests

# Alternatively, use requirements.txt
pip install -r requirements.txt
```

The script can now simply be called like this:

```
python contentdl.py
# or
py -3 contentdl.py
```

All source code and documentation in this repository is licensed under the [MIT license](LICENSE).

![ReadMe_Card](https://github-readme-stats.vercel.app/api/pin/?username=LucEast&repo=secasio-cdl&title_color=3e83c8&text_color=00cb71&icon_color=299bab&bg_color=171717&hide_border=true)