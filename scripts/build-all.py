from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for name in ['build-header.py','build-projects.py','build-dfo.py','build-activity.py','build-pengu.py']:
    subprocess.run([sys.executable,str(root/name)],check=True)
