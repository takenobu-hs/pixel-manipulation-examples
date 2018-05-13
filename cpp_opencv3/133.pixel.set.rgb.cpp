
#include <opencv2/opencv.hpp>


int main()
{
  cv::Mat im0;
  im0 = cv::Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(255, 255, 255));

  im0.at<cv::Vec3b>(200, 100) = cv::Vec3b(0, 0, 255);    // (y, x)

  cv::imwrite("z133.png", im0);
}

