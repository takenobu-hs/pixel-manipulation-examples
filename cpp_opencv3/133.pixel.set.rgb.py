
#include <opencv2/opencv.hpp>

int main()
{
  cv::Mat im0;
//im0 = cv::imread("img001.png", cv::IMREAD_GRAYSCALE);
//im0 = cv::Mat(cv::Size(640, 480), CV_8UC1, cv::Scalar(255));
  im0 = cv::Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(255, 255, 255));

//Vec3b p=Vec3b(0, 0, 255);
  im0.at<cv::Vec3b>(200, 100) = cv::Vec3b(0, 0, 255);    // (y, x)

  cv::imwrite("z107.png", im0);
}

