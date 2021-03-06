/*******************************************************************************
 *
 * Copyright (c) 2017, DbgVis - The Debugger Visualizer
 * Copyright (c) 2017, Peter Andreas Entschev
 * All rights reserved.
 *
 * BSD 3-Clause License
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * * Neither the name of the copyright holder nor the names of its
 *   contributors may be used to endorse or promote products derived from
 *   this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ******************************************************************************/

#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
#include <string>

cv::Mat read_image(const std::string& s)
{
    return cv::imread(s);
}

cv::Mat read_image_roi(const cv::Mat& img, cv::Rect roi)
{
    return cv::Mat(img(roi));
}

const cv::Mat* get_image_ptr(const cv::Mat& img)
{
    return &img;
}

void finalize()
{
}

int main(int argc, char *argv[])
{
    cv::Mat img = read_image("../samples/bansko.png");

    cv::Mat img_roi = read_image_roi(img, cv::Rect(100, 100, 100, 100));

    const cv::Mat* imgPtr = get_image_ptr(img);

    /// Just used as a breakpoint placeholder, do not remove
    finalize();

    return 0;
}
