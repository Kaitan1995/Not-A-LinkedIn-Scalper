# Virtual Environments 
- Can and oft best to make virtual environment sub folder within same file directory. For example, MettlerToledo virtual environment sub folder should be placed alongside MettlerToledo.py
- Must be on BASH
- test

1) Enter specific directory with -> cd Modbus/Ascenz/
2) Create virtual environment -> python -m venv MettlerToledoEnv
3) (Important) Launch virtual environment -> source MettlerToledoEnv/Scripts/Activate [Windows]
3) (Important) Launch virtual environment -> source MettlerToledoEnv/bin/Activate [Linux]
4) Install requirements (require actually making the file first) -> pip3 install -r ./requirements.txt --ignore-installed
5) (optional) Can use this to see package versions -> pip3 freeze
6) (Important) Deactivate virtual environment -> deactivate

# Create Python Executable 
- Using Windows/Linux with no multiprocessing -> pyinstaller --noconfirm --onefile --windowed ./Master_Datalogger.py
- If using Windows/Linux with multiprocessing you must add somewhere after <    if __name__ == "__main__":    > ->
  
if sys.platform.startswith('win'):
  freeze_support()
  print(chr(27) + "[2J")
  print("Simulate Master Datalogger") 
