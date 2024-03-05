from roboflow import Roboflow
rf = Roboflow(api_key="WkLe0BRUNAdlDtw2SDTQ")
project = rf.workspace("lev-counter").project("lev-counter-nylvi")
version = project.version(7)
dataset = version.download("yolov5")