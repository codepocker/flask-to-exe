# flask-to-exe
Install pywebview and pyinstaller on your system in order to convert your flask app into exe file using the following command
  pip install pyinstaller pywebview

After that import the webview module and start the webview module:
  import webview
  webview.start()
 
 Convert into One-file executable File
  pyinstaller app.py --onefile --windowed
  
  
 Note:
    If pyinstaller doesn't work, create a virtual environment first {python -m virtualenv virt}, activate the virt {source/Scripts/activate} and then install the modules in the virtual envirenment.
    After installing the modules in virt, run the command (pyinstaller app.py --onefile --windowed). It'll work correctly then.
