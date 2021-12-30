#include <iostream>
#include <string>

#include <boost/container/vector.hpp>
#include <boost/container/small_vector.hpp>
#include <boost/container/static_vector.hpp>
#include <boost/container/flat_set.hpp>
#include <boost/container/flat_map.hpp>

using namespace boost::container;

int main()
{
    flat_map<int, std::string> boost_flat_map_1{
        {111, "aaa"},
        {222, "bbb"},
        {333, "ccc"},
    };

    flat_set<int> boost_flat_set_1{
        111, 222, 333,
    };

    small_vector<int, 1> boost_small_vector_1{
        111, 222, 333,
    };

    small_vector<std::string, 1> boost_small_vector_2{
        "aaa", "bbb", "ccc",
    };

    static_vector<int, 10>
    boost_static_vector_1{
        111, 222, 333,
    };

    vector<std::string> boost_vector_1{
        "aaa", "bbb", "ccc",
    };

    return 0;
}
