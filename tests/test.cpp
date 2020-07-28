#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

#include "colorlib_map.hpp"

TEST_CASE("Colors codes are mapped properly", "[colorlib_gen]")
{
    SECTION("standard")
    {
        REQUIRE(cl_map("default")      == cl_colors::Default);
        REQUIRE(cl_map("prefix")       == cl_colors::Prefix);
        REQUIRE(cl_map("reply2cmd")    == cl_colors::Reply2cmd);
        REQUIRE(cl_map("showactivity") == cl_colors::Showactivity);
        REQUIRE(cl_map("error")        == cl_colors::Error);
        REQUIRE(cl_map("highlight")    == cl_colors::Highlight);
        REQUIRE(cl_map("player")       == cl_colors::Player);
        REQUIRE(cl_map("settings")     == cl_colors::Settings);
        REQUIRE(cl_map("command")      == cl_colors::Command);
        REQUIRE(cl_map("team 0")       == cl_colors::Team_0);
        REQUIRE(cl_map("team 1")       == cl_colors::Team_1);
        REQUIRE(cl_map("team 2")       == cl_colors::Default);
        REQUIRE(cl_map("teamcolor")    == cl_colors::Teamcolor);
    }
    SECTION("reference colors")
    {
        REQUIRE(cl_map("red")        == cl_colors::Red);
        REQUIRE(cl_map("lightred")   == cl_colors::Lightred);
        REQUIRE(cl_map("darkred")    == cl_colors::Darkred);
        REQUIRE(cl_map("bluegrey")   == cl_colors::Bluegrey);
        REQUIRE(cl_map("blue")       == cl_colors::Blue);
        REQUIRE(cl_map("darkblue")   == cl_colors::Darkblue);
        REQUIRE(cl_map("purple")     == cl_colors::Purple);
        REQUIRE(cl_map("orchid")     == cl_colors::Orchid);
        REQUIRE(cl_map("orange")     == cl_colors::Orange);
        REQUIRE(cl_map("yellow")     == cl_colors::Yellow);
        REQUIRE(cl_map("gold")       == cl_colors::Gold);
        REQUIRE(cl_map("lightgreen") == cl_colors::Lightgreen);
        REQUIRE(cl_map("green")      == cl_colors::Green);
        REQUIRE(cl_map("lime")       == cl_colors::Lime);
        REQUIRE(cl_map("grey")       == cl_colors::Grey);
        REQUIRE(cl_map("grey2")      == cl_colors::Grey2);
    }
    SECTION("engine colors")
    {
        REQUIRE(cl_map("engine 1")  == cl_colors::Engine_1);
        REQUIRE(cl_map("engine 2")  == cl_colors::Engine_2);
        REQUIRE(cl_map("engine 3")  == cl_colors::Engine_3);
        REQUIRE(cl_map("engine 4")  == cl_colors::Engine_4);
        REQUIRE(cl_map("engine 5")  == cl_colors::Engine_5);
        REQUIRE(cl_map("engine 6")  == cl_colors::Engine_6);
        REQUIRE(cl_map("engine 7")  == cl_colors::Engine_7);
        REQUIRE(cl_map("engine 8")  == cl_colors::Engine_8);
        REQUIRE(cl_map("engine 9")  == cl_colors::Engine_9);
        REQUIRE(cl_map("engine 10") == cl_colors::Engine_10);
        REQUIRE(cl_map("engine 11") == cl_colors::Engine_11);
        REQUIRE(cl_map("engine 12") == cl_colors::Engine_13);
        REQUIRE(cl_map("engine 14") == cl_colors::Engine_14);
        REQUIRE(cl_map("engine 15") == cl_colors::Engine_15);
        REQUIRE(cl_map("engine 16") == cl_colors::Engine_16);
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
    REQUIRE(cl_map("blueblue")    == null);
    REQUIRE(cl_map("Red")         == null);
    REQUIRE(cl_map("Hello World") == null);
}
