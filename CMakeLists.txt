cmake_minimum_required(VERSION 2.8)

project(DbgVis)

set(CMAKE_BUILD_TYPE "Debug" CACHE STRING
    "Choose the type of build, options are: Debug Release RelWithDebInfo MinSizeRel."
    FORCE)

find_package(OpenCV)

set(EXAMPLES_DIR examples)

add_executable(cv_imread ${EXAMPLES_DIR}/cv_imread.cpp)
target_link_libraries(cv_imread ${OpenCV_LIBS})

set(SAMPLES_DIR samples)
set(SAMPLE_FILES ${SAMPLES_DIR}/bansko.png)
