#include <iostream>
#include <vector>

using namespace std;

struct Param {
	int n{};
	vector<char> v{};

	friend istream& operator>>( istream& is, Param& self )
	{
		is >> self.n;

		char elm{};
		is >> elm;

		while ( elm != '\n' and elm != '\0' ) {
			if ( elm == ' ' ) {
				elm = static_cast<char>( is.get() );
				continue;
			}

			self.v.push_back( elm );

			elm = static_cast<char>( is.get() );
		}

		return is;
	}
};

struct Result {
	int x{}, y{};

	bool operator==( const Result& other ) const
	{
		return ( x == other.x ) && ( y == other.y );
	}

	friend istream& operator>>( istream& is, Result& self )
	{
		is >> self.y >> self.x;

		return is;
	}
};

template <>
struct std::formatter<Result> {
	constexpr auto parse( format_parse_context& ctx ) { return ctx.begin(); }

	template <typename FormatContext>
	auto format( const Result& ts, FormatContext& ctx ) {
		auto out = format_to( ctx.out(), "{} {}", ts.y, ts.x );
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
	const int x_max{ param.n }, y_max{ param.n };
	Result pos{ 1, 1 };

	for ( const auto& dir : param.v ) {
		switch ( dir ) {
		case 'R':
			pos.x += 1;
			break;
		case 'L':
			pos.x -= 1;
			break;
		case 'U':
			pos.y -= 1;
			break;
		case 'D':
			pos.y += 1;
			break;
		}

		pos.x = clamp( pos.x, 1, x_max );
		pos.y = clamp( pos.y, 1, y_max );
	}

	return pos;
}

Result BookSolution( Param param )
{
	return Result{};
}
