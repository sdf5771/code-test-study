#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Param {
	int n{};

	struct Score {
		string name{};
		int score{};
	};

	vector<Score> v{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n;

		string name{};
		int score{};
		for ( int i{}; i < p.n; ++i ) {
			is >> name >> score;
			p.v.push_back( { name, score } );
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

		auto out = format_to( ctx.out(), "");

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
}

Result MySolution( Param param )
{
	Result v{};

	sort( param.v.begin(), param.v.end(), [](Param::Score& lhs, Param::Score& rhs) {
		return lhs.score < rhs.score;
		} );

	for ( const auto& e : param.v )
		v.push_back( e.name );

	return v;
}

Result BookSolution( Param param )
{
	return Result{};
}
