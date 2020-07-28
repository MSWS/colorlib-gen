cmake_minimum_required(VERSION 3.10)

# Project name
project(ColorLib-Gen
    VERSION 1.0.0
    DESCRIPTION ""
    LANGUAGES C CXX
)

# Catch2 needed for testing
find_package(Catch2 CONFIG REQUIRED)

# Do stuff depending on the compiler
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU" OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "-W -Wall -Wextra -Wpedantic -Wunused-value -Wold-style-cast -std=c++17")
    set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
    set(CMAKE_CXX_FLAGS_RELEASE "-O3")
elseif(CMAKE_CXX_COMPILER_ID MATCHES "MSVC")
    set(CMAKE_CXX_FLAGS "/W4 /EHsc /std:c++17")
    set(CMAKE_CXX_FLAGS_DEBUG "/O0 /ZI")
    set(CMAKE_CXX_FLAGS_RELEASE "/O2 /Ob2")
endif()

add_executable(colorlib_gen_tests
    test.cpp
)

target_include_directories(colorlib_gen_tests PUBLIC
    {CMAKE_CURRENT_LIST_DIR}
)

target_link_libraries(colorlib_gen_tests PUBLIC
    Catch2::Catch2
)

include(CTest)
include(Catch)
catch_discover_tests(colorlib_gen_tests)
