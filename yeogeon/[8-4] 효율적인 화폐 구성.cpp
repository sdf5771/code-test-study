#include <iostream>
#include <vector>

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
	vector<int> v( param.k + 1, 10001 );
	v[0] = 0;

	for ( int i{1}; i <= param.k; ++i ) {
		for ( const auto money : param.v )
			if ( i - money >= 0 )
				v[i] = min( v[i], v[i - money] + 1 );
	}

	return v.back() == 10001 ? -1 : v.back();
}

Result BookSolution( Param param )
{
	return 0;
}
