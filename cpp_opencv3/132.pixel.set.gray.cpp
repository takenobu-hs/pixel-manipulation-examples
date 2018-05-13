
#include <opencv2/opencv.hpp>


int main()
{
  cv::Mat im0;
  im0 = cv::Mat(cv::Size(640, 480), CV_8UC1, cv::Scalar(255));

  im0.at<uchar>(200, 100) = 0;    // (y, x)

  cv::imwrite("z132.png", im0);
}

