
#include <opencv2/opencv.hpp>


int main(void)
{
  cv::Mat im0(cv::Size(640, 480), CV_8UC3, cv::Scalar(0, 255, 0));

  cv::imwrite("z120.png", im0);
}


