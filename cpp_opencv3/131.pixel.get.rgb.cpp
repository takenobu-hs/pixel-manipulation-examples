
#include <opencv2/opencv.hpp>


int main()
{
  cv::Mat im0;
//im0 = cv::imread("../images/img001.png", cv::IMREAD_GRAYSCALE);
  im0 = cv::imread("../images/img001.png", cv::IMREAD_COLOR);

  cv::Vec3b p = im0.at<cv::Vec3b>(200, 100);
  int r, g, b;
  r = p(2);
  g = p(1);
  b = p(0);

  std::printf("(%d, %d, %d)\n", r, g, b);

}

