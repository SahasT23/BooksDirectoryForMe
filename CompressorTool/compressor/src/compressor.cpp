/* === compression/src/compressor.cpp === */
#include "compressor.hpp"
#include <fstream>
#include <filesystem>
#include <stdexcept>

void compression::compress_file(const std::string& input, const std::string& output) {
    std::ifstream src(input, std::ios::binary);
    if (!src) throw std::runtime_error("Failed to open input file: " + input);
    std::ofstream dst(output, std::ios::binary);
    if (!dst) throw std::runtime_error("Failed to open output file: " + output);
    dst << src.rdbuf();
}

void compression::decompress_file(const std::string& input, const std::string& output) {
    std::ifstream src(input, std::ios::binary);
    if (!src) throw std::runtime_error("Failed to open input file: " + input);
    std::ofstream dst(output, std::ios::binary);
    if (!dst) throw std::runtime_error("Failed to open output file: " + output);
    dst << src.rdbuf();
}
