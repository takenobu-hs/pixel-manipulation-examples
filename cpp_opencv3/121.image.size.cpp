
#include <opencv2/opencv.hpp>
#include <cstdio>


int main(void)
{
  cv::Mat im0(cv::Size(640, 480), CV_8UC3, cv::Scalar(0, 255, 0));

  int width  = im0.cols;
  int height = im0.rows;
  std::printf("(%d, %d)\n", width, height);

  cv::imwrite("z121.png", im0);
}

