cmake_minimum_required(VERSION 3.12)
project(mycompressor)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(compression)

include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG v2.11.1
)
FetchContent_MakeAvailable(pybind11)

pybind11_add_module(mycompressor bindings/bindings.cpp)
target_include_directories(mycompressor PRIVATE compression/include)
target_link_libraries(mycompressor PRIVATE compression_lib)
