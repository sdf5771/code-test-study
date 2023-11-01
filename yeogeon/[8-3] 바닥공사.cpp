#include <iostream>
#include <vector>
#include "CodingTester.h"

using namespace std;

using Param = unsigned long long int;
using Result = unsigned long long int;

Result MySolution( Param param );
Result BookSolution( Param param );

int main()
{
	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;
}

Result MySolution( Param param )
{
	vector<unsigned long long int> v( param + 1, 0 );

	v[1] = 1;
	if ( param >= 2 )
		v[2] = 3;

	for ( int i{ 3 }; i <= param; ++i ) {
		v[i] = v[i - 1] + v[i - 2] * 2;
	}

	return v[param] % 796796;
}

Result BookSolution( Param param )
{
	vector<int> v( param + 1, 0 );
	return v[param];
}
