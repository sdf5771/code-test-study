#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Param {
	int n{}, k{};
	vector<int> v1{};
	vector<int> v2{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n;

		int elm{};
		for ( int i{}; i < p.n; ++i ) {
			is >> elm;
			p.v1.push_back( elm );
		}

		is >> p.k;

		elm = {};
		for ( int i{}; i < p.k; ++i ) {
			is >> elm;
			p.v2.push_back( elm );
		}

		return is;
	}
};

using Result = vector<string>;

template <>
struct std::formatter<Result> {
	constexpr auto parse( format_parse_context& ctx ) { return ctx.begin(); }

	template <typename FormatContext>
	auto format( const Result& ts, FormatContext& ctx ) {

		auto out = format_to( ctx.out(), "" );
		for ( const auto& s : ts )
			out = format_to( out, "{} ", s );

		return out;
	}
};

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

Result MySolution( Param param )
{
	Result answers{};

	sort( param.v1.begin(), param.v1.end() );

	for ( auto i : param.v2 )
		if ( binary_search( param.v1.begin(), param.v1.end(), i ) )
			answers.push_back( "yes" );
		else
			answers.push_back( "no" );



	return answers;
}

Result BookSolution( Param param )
{
	return Result{};
}
