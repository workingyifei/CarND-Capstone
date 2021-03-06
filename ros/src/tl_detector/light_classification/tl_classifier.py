from styx_msgs.msg import TrafficLight
from simple_detector import simple_detector

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        
        result = simple_detector(image)
        if result == 0:
            return TrafficLight.RED
        if result == 1:
            return TrafficLight.YELLOW
        if result == 2:
            return TrafficLight.GREEN

        return TrafficLight.UNKNOWN
