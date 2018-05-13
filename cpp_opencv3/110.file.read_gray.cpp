
#include <opencv2/opencv.hpp>


int main()
{
  cv::Mat im0;
//im0 = cv::imread("../images/img001.png", cv::IMREAD_COLOR);
  im0 = cv::imread("../images/img001.png", cv::IMREAD_GRAYSCALE);

  cv::imwrite("z110.png", im0);
}

