
#include <opencv2/opencv.hpp>


int main(void)
{
  cv::Mat im0;
  im0 = cv::imread("../images/img001.png", 1);

  if(im0.empty()) return -1;

  cv::imwrite("z100.png", im0);
}

