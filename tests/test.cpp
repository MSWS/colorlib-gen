#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

#include "colorlib_map.hpp"

TEST_CASE("Colors codes are mapped properly", "[colorlib_gen]")
{
    SECTION("standard")
    {
        REQUIRE(cl_map("default")      == std::make_tuple(cl_colors::Default,      8));
        REQUIRE(cl_map("prefix")       == std::make_tuple(cl_colors::Prefix,       7));
        REQUIRE(cl_map("reply2cmd")    == std::make_tuple(cl_colors::Reply2cmd,    10));
        REQUIRE(cl_map("showactivity") == std::make_tuple(cl_colors::Showactivity, 13));
        REQUIRE(cl_map("error")        == std::make_tuple(cl_colors::Error,        6));
        REQUIRE(cl_map("highlight")    == std::make_tuple(cl_colors::Highlight,    10));
        REQUIRE(cl_map("player")       == std::make_tuple(cl_colors::Player,       7));
        REQUIRE(cl_map("settings")     == std::make_tuple(cl_colors::Settings,     9));
        REQUIRE(cl_map("command")      == std::make_tuple(cl_colors::Command,      8));
        REQUIRE(cl_map("team 0")       == std::make_tuple(cl_colors::Team_0,       7));
        REQUIRE(cl_map("team 1")       == std::make_tuple(cl_colors::Team_1,       7));
        REQUIRE(cl_map("team 2")       == std::make_tuple(cl_colors::Team_2,       7));
        REQUIRE(cl_map("teamcolor")    == std::make_tuple(cl_colors::Teamcolor,    10));
    }
    SECTION("reference colors")
    {
        REQUIRE(cl_map("red")        == std::make_tuple(cl_colors::Red,        4));
        REQUIRE(cl_map("lightred")   == std::make_tuple(cl_colors::Lightred,   9));
        REQUIRE(cl_map("darkred")    == std::make_tuple(cl_colors::Darkred,    8));
        REQUIRE(cl_map("bluegrey")   == std::make_tuple(cl_colors::Bluegrey,   9));
        REQUIRE(cl_map("blue")       == std::make_tuple(cl_colors::Blue,       5));
        REQUIRE(cl_map("darkblue")   == std::make_tuple(cl_colors::Darkblue,   9));
        REQUIRE(cl_map("purple")     == std::make_tuple(cl_colors::Purple,     7));
        REQUIRE(cl_map("orchid")     == std::make_tuple(cl_colors::Orchid,     7));
        REQUIRE(cl_map("orange")     == std::make_tuple(cl_colors::Orange,     7));
        REQUIRE(cl_map("yellow")     == std::make_tuple(cl_colors::Yellow,     7));
        REQUIRE(cl_map("gold")       == std::make_tuple(cl_colors::Gold,       5));
        REQUIRE(cl_map("lightgreen") == std::make_tuple(cl_colors::Lightgreen, 11));
        REQUIRE(cl_map("green")      == std::make_tuple(cl_colors::Green,      6));
        REQUIRE(cl_map("lime")       == std::make_tuple(cl_colors::Lime,       5));
        REQUIRE(cl_map("grey")       == std::make_tuple(cl_colors::Grey,       5));
        REQUIRE(cl_map("grey2")      == std::make_tuple(cl_colors::Grey2,      6));
    }
    SECTION("engine colors")
    {
        REQUIRE(cl_map("engine 1")  == std::make_tuple(cl_colors::Engine_1,  9));
        REQUIRE(cl_map("engine 2")  == std::make_tuple(cl_colors::Engine_2,  9));
        REQUIRE(cl_map("engine 3")  == std::make_tuple(cl_colors::Engine_3,  9));
        REQUIRE(cl_map("engine 4")  == std::make_tuple(cl_colors::Engine_4,  9));
        REQUIRE(cl_map("engine 5")  == std::make_tuple(cl_colors::Engine_5,  9));
        REQUIRE(cl_map("engine 6")  == std::make_tuple(cl_colors::Engine_6,  9));
        REQUIRE(cl_map("engine 7")  == std::make_tuple(cl_colors::Engine_7,  9));
        REQUIRE(cl_map("engine 8")  == std::make_tuple(cl_colors::Engine_8,  9));
        REQUIRE(cl_map("engine 9")  == std::make_tuple(cl_colors::Engine_9,  9));
        REQUIRE(cl_map("engine 10") == std::make_tuple(cl_colors::Engine_10, 10));
        REQUIRE(cl_map("engine 11") == std::make_tuple(cl_colors::Engine_11, 10));
        REQUIRE(cl_map("engine 12") == std::make_tuple(cl_colors::Engine_12, 10));
        REQUIRE(cl_map("engine 13") == std::make_tuple(cl_colors::Engine_13, 10));
        REQUIRE(cl_map("engine 14") == std::make_tuple(cl_colors::Engine_14, 10));
        REQUIRE(cl_map("engine 15") == std::make_tuple(cl_colors::Engine_15, 10));
        REQUIRE(cl_map("engine 16") == std::make_tuple(cl_colors::Engine_16, 10));
    }
}

TEST_CASE("Bad color codes return null terminator", "[colorlib_gen]")
{
    // these cases are more just basic checks as the optimiser may allow some
    // bad tags, due to skipping redundant decisions for example {blie} would
    // be parsed the same as {blue} with the example config as the 'lu' never
    // needed to be checked, thus the behaviour for some bad tags can be
    // undefined, it is up to the user to type them correctly.

    constexpr auto null = static_cast<cl_colors>(0);
    REQUIRE(cl_map("blueblue")    == std::make_tuple(null, 0));
    REQUIRE(cl_map("Red")         == std::make_tuple(null, 0));
    REQUIRE(cl_map("Hello World") == std::make_tuple(null, 0));
}
