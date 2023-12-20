from roboflow import Roboflow
rf = Roboflow(api_key="cYLZHzsX9MSUKu68YhbX")
project = rf.workspace("indianfoodnet").project("indianfoodnet")
dataset = project.version(1).download("yolov8")