#include <iostream>
#include <vector>
#include "CodingTester.h"

using namespace std;

struct Param {
	int n{};
	int k{};

	friend istream& operator>>( istream& is, Param& self )
	{
		is >> self.n >> self.k;

		return is;
	}
};

int MySolution( Param param );
int BookSolution( Param param );

int main()
{
	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;
}

int MySolution( Param param )
{
	int dividend = param.n;
	int divisor = param.k;
	int remainder{}, amount{};
	
	do {
		remainder = dividend % divisor;
		dividend /= divisor;
		amount += remainder + (dividend < 1 ? -1 : 1);
	} while ( dividend > 1 );

	return amount;
}

int BookSolution( Param param )
{
	return 0;
}
