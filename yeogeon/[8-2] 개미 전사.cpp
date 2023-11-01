#include <iostream>
#include <vector>

using namespace std;

struct Param {
	int n{};
	vector<int> v{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n;

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
	vector<int> v( param.n, 0 );

	v[0] = param.v[0];
	v[1] = max( param.v[0], param.v[1] );

	for ( int i{ 2 }; i < param.n; ++i ) {
		v[i] = max( v[i - 1], v[i - 2] + param.v[i] );
	}

	return v[param.n - 1];
}

Result BookSolution( Param param )
{
	return 0;
}
