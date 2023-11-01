#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Param {
	int n{}, k{};
	vector<int> v1{};
	vector<int> v2{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n >> p.k;

		int elm{};
		for ( int i{}; i < p.n; ++i ) {
			is >> elm;
			p.v1.push_back( elm );
		}

		elm = {};
		for ( int i{}; i < p.n; ++i ) {
			is >> elm;
			p.v2.push_back( elm );
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
	Result cnt{};


	for ( int i{}; i < param.k; ++i )
		swap( *min_element( param.v1.begin(), param.v1.end() ), *max_element( param.v2.begin(), param.v2.end() ) );

	cnt = accumulate( param.v1.begin(), param.v1.end(), 0 );

	return cnt;
}

Result BookSolution( Param param )
{
	return Result{};
}
