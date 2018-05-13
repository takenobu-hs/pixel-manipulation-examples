
#include <opencv2/opencv.hpp>


int main()
{
  cv::Mat im0;
  im0 = cv::imread("../images/img001.png", cv::IMREAD_GRAYSCALE);

  unsigned int p;
  p = im0.at<uchar>(200, 100);    // (y, x)
  std::printf("(%d)\n", p);

}

