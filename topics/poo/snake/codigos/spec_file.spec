# spec_file.spec
import os
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Get the absolute path to the directory containing your script
root_dir = Path(sys.argv[0]).resolve().parent

# Include necessary files
datas = collect_data_files('pygame') + [(str(root_dir / "assets"), "assets")]

exe = os.path.join('dist', 'main.exe')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='snake')

app = BUNDLE(coll,
             name='snake.app',
             icon=None,
             bundle_identifier=None)

# Now you need to add the necessary datas for your Pygame project
# You'll need to include the font, image, sound and music files your game uses
