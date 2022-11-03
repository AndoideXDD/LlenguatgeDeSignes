from Detector import *

modelUrl = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz"


clasFile = "coco.names"
imagesPath = "test\cama-doble-marco-madera-sabanas-blancas-aislado_176382-170.webp"
threshold = 0.5 

detector = Detector()
detector.readClasses(clasFile)
detector.DownloadModel(modelUrl) 
detector.loadModel()
detector.predictImage(imagesPath, threshold)
