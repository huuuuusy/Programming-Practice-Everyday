#define CATCH_CONFIG_MAIN
#include "../Catch2/single_include/catch2/catch.hpp"
#include "V1.h"

TEST_CASE("fixedPoint", "fixedPoint")
{
    Solution s;

    std::vector<int> v1{-10, -5, 0, 3, 7};
    REQUIRE( (s.fixedPoint(v1) ==  3) );

    std::vector<int> v2{0, 2, 5, 8, 17};
    REQUIRE( (s.fixedPoint(v2) ==  0) );

    std::vector<int> v3{-10, -5, 3, 4, 7, 9};
    REQUIRE( (s.fixedPoint(v3) == -1) );
}