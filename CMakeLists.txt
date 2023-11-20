cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

# to replace `-DCMAKE_BUILD_TYPE=Release` in `cmake -DCMAKE_BUILD_TYPE=Release ..`
set(CMAKE_BUILD_TYPE "Release")

project(tglang VERSION 2.0.0 LANGUAGES C)

# Set to max optimize level
if(CMAKE_C_COMPILER_ID STREQUAL "GNU")
    add_compile_options(-O3)
elseif(CMAKE_C_COMPILER_ID STREQUAL "Clang")
    add_compile_options(-O3)
elseif(MSVC)
    add_compile_options(/O2)
endif()

add_library(tglang SHARED tglang.c)
#add_executable(tglang tglang.c)
