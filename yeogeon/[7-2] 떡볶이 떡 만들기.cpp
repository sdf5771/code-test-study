#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Param {
	int n{}, k{};
	vector<int> v{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n >> p.k;

		int elm{};
		for ( int i{}; i < p.n; ++i ) {
			is >> elm;
			p.v.push_back( elm );
		}

		return is;
	}
};

using Result = int;

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
	int start{};
	int end = *max_element( param.v.begin(), param.v.end() );
	Result mid{};

	while ( true ) {
		mid = (start + end) / 2;
		int amount = accumulate( param.v.begin(), param.v.end(), 0, [&]( const int& a, const int& b ) {
			return a + max( b - mid, 0 );
			} );

		if ( amount == param.k )
			break;
		else if ( amount > param.k )
			start = mid + 1;
		else
			end = mid - 1;
	}

	return mid;
}

Result BookSolution( Param param )
{
	return Result{};
}
