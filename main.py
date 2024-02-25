from roboflow import Roboflow
rf = Roboflow(api_key="WkLe0BRUNAdlDtw2SDTQ")
version = project.version(1)
version.deploy("model-type", "lev-counter-2")