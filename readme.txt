You need to put your ffmpeg in /ffmpeg,like /bin,/doc,/include,/lib,LICENSE.txt

Some packages are needed:
     pip install -r requirements.txt

Use command:
     python setup.py build_ext --inplace
Then you will find some x.pyd  and x.c files

If you want to use *.ui,launch your Qt Designer and open it:
    For how to use PyQt-Fluent-Widgets in Qt Designer,visit https://pyqt-fluent-widgets.readthedocs.io/en/latest

Launch with Main.py

MANY BUGS MABE!!!
