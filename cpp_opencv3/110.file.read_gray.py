
#include <opencv2/opencv.hpp>

int main()
{
  cv::Mat im0;
//im0 = cv::imread("img001.png", cv::IMREAD_COLOR);
  im0 = cv::imread("img001.png", cv::IMREAD_GRAYSCALE);

  cv::imwrite("z103.png", im0);
}

