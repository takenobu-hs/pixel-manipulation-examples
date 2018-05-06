
#include <opencv2/opencv.hpp>

int main()
{
  cv::Mat im0;
//im0 = cv::imread("img001.png", cv::IMREAD_GRAYSCALE);
//im0 = Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(0, 255, 0));
  im0 = cv::Mat(cv::Size(640, 480), CV_8UC1, cv::Scalar(255));

  im0.at<uchar>(200, 100) = 0;    // (y, x)

  cv::imwrite("z106.png", im0);
}

