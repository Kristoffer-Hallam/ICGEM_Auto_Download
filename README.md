# ICGEM data download automation

The project's goal is to make potential field geophysicist life easier by automating data download from [ICGEM website](http://icgem.gfz-potsdam.de/home). The user will be asked to input some important information in order to download the desired data. This is the first version and it only contemplates **Regular grid** data download. However, we intend to extend the code for *User-defined points* data download as well.


## Installation
<img align="center" height=240 src="iu.jpeg"/>
One must have **selenium**, **webdriver** and **webdriver_manager** installed to run the code. If that is not the case, please follow the steps bellow on your terminal or cmd window.

```bash
pip install selenium webdriver webdriver_manager
```

If you have Anaconda installed then you can easily search for these packages in the App.