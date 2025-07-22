#include <pybind11/pybind11.h>
#include "compressor.hpp"

namespace py = pybind11;

PYBIND11_MODULE(mycompressor, m) {
    m.doc() = "A simple compression module using C++";
    m.def("compress_file", &compression::compress_file, "Compress a file");
    m.def("decompress_file", &compression::decompress_file, "Decompress a file");
}
