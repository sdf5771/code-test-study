#include <iostream>
#include <vector>

using namespace std;

using Param = int;
using Result = int;

Result MySolution( Param param );
Result BookSolution( Param param );

int main()
{
	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;

	cout << "Book's Solution ===========\n";
	cout << BookSolution( p ) << endl << endl;
}

Result MySolution( Param param )	// wrong
{
	Result result{};

	while ( param > 1 ) {
		int i = param - 1;

		if ( param % 5 == 0 )
			param /= 5;
		else if ( i % 5 == 0 )
			param -= 1;
		else if ( param % 3 == 0 )
			param /= 3;
		else if ( i % 3 == 0 )
			param -= 1;
		else if ( param % 2 == 0 )
			param /= 2;
		else
			param -= 1;
		++result;
	}

	return result;
}

Result BookSolution( Param param )
{
	vector<int> v( param + 1 , 0 );

	int i{ 2 };
	while ( i <= param ) {
		// X - 1
		v[i] = v[i - 1] + 1;

		// X / 5
		if ( i % 5 == 0 )
			v[i] = min( v[i], v[i / 5] + 1 );

		// X / 3
		if ( i % 3 == 0 )
			v[i] = min( v[i], v[i / 3] + 1 );

		// X / 2
		if ( i % 2 == 0 )
			v[i] = min( v[i], v[i / 2] + 1 );

		++i;
	}

	return v[param];
}
