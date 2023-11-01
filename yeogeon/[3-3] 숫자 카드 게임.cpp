#include <iostream>
#include <vector>

using namespace std;

struct Param {
	int n{};
	int k{};
	vector<vector<int>> v{};

	friend istream& operator>>( istream& is, Param& self )
	{
		is >> self.n >> self.k;

		int elm{};
		for ( int n{}; n < self.n; ++n ) {
			self.v.push_back( {} );
			for ( int m{}; m < self.k; ++m ) {
				is >> elm;
				self.v[n].emplace_back(elm);
			}
		}

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

	cout << "Book's Solution ===========\n";
	cout << BookSolution( p ) << endl << endl;
}

int MySolution( Param param )
{
	auto v = param.v;
	vector<int> mins{};

	for ( auto elm : v )
		mins.emplace_back( *min_element(elm.begin(), elm.end()) );
	
	return *max_element( mins.begin(), mins.end() );
}

int BookSolution( Param param )
{
	auto v = param.v;
	int result{};

	for ( auto elm : v )
		result = max( *min_element( elm.begin(), elm.end() ), result );

	return result;
}
