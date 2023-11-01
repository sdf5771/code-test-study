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

using Result = vector<int>;

template <>
struct std::formatter<Result> {
	constexpr auto parse( format_parse_context& ctx ) { return ctx.begin(); }

	template <typename FormatContext>
	auto format( const Result& ts, FormatContext& ctx ) {

		auto out = format_to( ctx.out(), "");
		for ( const auto i : ts )
			out = format_to( out, "{} ", i );

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
	Result v{ param.v };

	sort( v.begin(), v.end(), greater() );

	return v;
}

Result BookSolution( Param param )
{
	return Result{};
}
