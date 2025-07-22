// compressor.hpp
#pragma once
#include <string>

namespace compression {
    void compress_file(const std::string& input, const std::string& output);
    void decompress_file(const std::string& input, const std::string& output);
}
